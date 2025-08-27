"""Prefect helpers."""
from __future__ import annotations

from typing import Any, Callable, TypeVar

from prefect import flow, get_run_logger, task

T = TypeVar("T")


def task_default(**overrides: Any) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Factory for Prefect tasks with sane defaults."""
    defaults: dict[str, Any] = {
        "retries": 2,
        "retry_delay_seconds": 5,
        "timeout_seconds": 600,
    }
    defaults.update(overrides)
    return task(**defaults)


def flow_default(
    fn: Callable[..., T] | None = None,
    *,
    name: str | None = None,
    tags: list[str] | None = None,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator adding logging around Prefect flows."""

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        flow_name = name or func.__name__

        @flow(name=flow_name, tags=tags)
        def wrapped(*args: Any, **kwargs: Any) -> T:
            logger = get_run_logger()
            logger.info("Starting %s", flow_name)
            logger.info("args=%s kwargs=%s", args, kwargs)
            result = func(*args, **kwargs)
            logger.info("Finished %s", flow_name)
            return result

        return wrapped

    if fn is not None:
        return decorator(fn)
    return decorator
