"""Common type aliases and protocols."""
from __future__ import annotations

import os
from typing import Any, Protocol, TypeAlias, runtime_checkable

PathLike: TypeAlias = str | os.PathLike[str]

JsonValue: TypeAlias = (
    str
    | int
    | float
    | bool
    | None
    | list["JsonValue"]
    | dict[str, "JsonValue"]
)
Jsonable: TypeAlias = JsonValue


@runtime_checkable
class SupportsWrite(Protocol):
    """Protocol for objects with a ``write`` method."""

    def write(self, s: str, /) -> Any:  # pragma: no cover - protocol definition
        """Write a string."""
        ...
