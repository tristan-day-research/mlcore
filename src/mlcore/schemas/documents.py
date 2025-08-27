"""Document schemas."""
from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import Field

from .base import BaseSchema


class ModelCard(BaseSchema):
    """Metadata describing a model."""

    name: str
    version: str
    metrics: dict[str, float] = Field(default_factory=dict)
    params: dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class DataBatch(BaseSchema):
    """Information about a data batch."""

    n_rows: int
    schema_version: str
    source: str | None = None
