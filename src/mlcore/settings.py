"""Application settings using pydantic-settings."""
from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Application configuration."""

    env: Literal["dev", "prod"] = "dev"
    data_dir: Path = Path("data")
    s3_bucket: str | None = None

    model_config = SettingsConfigDict(env_file=".env")

    @classmethod
    def from_env(cls) -> "AppSettings":
        """Load settings from environment and optional ``.env`` file."""
        return cls()
