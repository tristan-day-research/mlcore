"""Public API for mlcore."""
from ._version import __version__
from .io.files import read_df, read_json, write_df, write_json
from .schemas.documents import DataBatch, ModelCard
from .settings import AppSettings
from .utils.logging import get_logger
from .validation.records import validate_iterable

try:  # pragma: no cover - optional dependency
    from .integrations.prefect.tasks import flow_default, task_default
except Exception:  # pragma: no cover
    task_default = flow_default = None

__all__ = [
    "__version__",
    "get_logger",
    "AppSettings",
    "read_df",
    "write_df",
    "read_json",
    "write_json",
    "ModelCard",
    "DataBatch",
    "validate_iterable",
    "task_default",
    "flow_default",
]
