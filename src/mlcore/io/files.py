"""File IO helpers."""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from ..types import Jsonable, PathLike


def read_df(path: PathLike) -> pd.DataFrame:
    """Read a DataFrame from a CSV or Parquet file."""
    file_path = Path(path)
    if file_path.suffix == ".csv":
        return pd.read_csv(file_path)
    if file_path.suffix in {".parquet", ".pq"}:
        return pd.read_parquet(file_path)
    raise ValueError(f"Unsupported extension: {file_path.suffix}")


def write_df(df: pd.DataFrame, path: PathLike) -> None:
    """Write a DataFrame to CSV or Parquet."""
    file_path = Path(path)
    if file_path.suffix == ".csv":
        df.to_csv(file_path, index=False)
    elif file_path.suffix in {".parquet", ".pq"}:
        df.to_parquet(file_path, index=False)
    else:
        raise ValueError(f"Unsupported extension: {file_path.suffix}")


def read_json(path: PathLike) -> Jsonable:
    """Read JSON data from a file."""
    with Path(path).open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(obj: Jsonable, path: PathLike) -> None:
    """Write JSON data to a file."""
    with Path(path).open("w", encoding="utf-8") as f:
        json.dump(obj, f)


# TODO: add fsspec/S3 support
