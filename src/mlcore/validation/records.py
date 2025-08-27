"""Validation helpers."""
from __future__ import annotations

from typing import Any, Iterable

from pydantic import BaseModel, ValidationError


def validate_iterable(rows: Iterable[dict[str, Any]], model: type[BaseModel]) -> list[dict[str, Any]]:
    """Validate each row against ``model``.

    Parameters
    ----------
    rows:
        Iterable of dictionaries to validate.
    model:
        ``pydantic`` model used for validation.

    Returns
    -------
    list[dict[str, Any]]
        Validated items as plain dictionaries.
    """
    validated: list[dict[str, Any]] = []
    for idx, row in enumerate(rows):
        try:
            obj = model.model_validate(row)
        except ValidationError as exc:  # pragma: no cover - exercised in tests
            errors = []
            for err in exc.errors():
                err = dict(err)
                err["loc"] = ("row", idx, *err["loc"])
                errors.append(err)
            raise ValidationError.from_exception_data(model.__name__, errors)
        else:
            validated.append(obj.model_dump())
    return validated
