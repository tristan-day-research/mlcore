"""Base schema utilities."""
from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel


def ts_utcnow() -> datetime:
    """Return the current UTC time."""
    return datetime.utcnow()


class BaseSchema(BaseModel):
    """Mixin providing helpers for schemas."""

    def as_dict(self) -> dict[str, Any]:
        """Return a plain dictionary representation."""
        return self.model_dump()
