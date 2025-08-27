"""Logging utilities."""
from __future__ import annotations

import json
import logging
import os


def _use_json(param: bool | None) -> bool:
    if param is not None:
        return param
    return os.getenv("MLCORE_JSON_LOGS", "false").lower() == "true"


class _JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:  # pragma: no cover - simple
        message = {
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
        }
        return json.dumps(message)


def get_logger(name: str, json: bool | None = None) -> logging.Logger:
    """Return a configured logger.

    Parameters
    ----------
    name:
        Logger name.
    json:
        Force JSON output. If ``None`` the ``MLCORE_JSON_LOGS`` environment
        variable controls the format.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter: logging.Formatter
        if _use_json(json):
            formatter = _JsonFormatter()
        else:
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False
    return logger
