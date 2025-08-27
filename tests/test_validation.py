import pytest
from pydantic import BaseModel, ValidationError

from mlcore import validate_iterable


class Row(BaseModel):
    a: int


def test_validate_iterable_success() -> None:
    rows = [{"a": 1}, {"a": 2}]
    result = validate_iterable(rows, Row)
    assert result == rows


def test_validate_iterable_failure() -> None:
    rows = [{"a": 1}, {"a": "x"}]
    with pytest.raises(ValidationError) as exc:
        validate_iterable(rows, Row)
    err = exc.value.errors()[0]
    assert err["loc"][0] == "row"
    assert err["loc"][1] == 1
