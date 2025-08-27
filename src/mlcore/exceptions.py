"""Custom exceptions for mlcore."""

class MlcoreError(Exception):
    """Base exception for mlcore."""


class ConfigurationError(MlcoreError):
    """Raised when configuration is invalid."""
