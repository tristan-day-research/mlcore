import pandas as pd

from mlcore import read_df, read_json, write_df, write_json


def test_df_round_trip(tmp_path) -> None:
    df = pd.DataFrame({"a": [1, 2]})
    path = tmp_path / "test.csv"
    write_df(df, path)
    out = read_df(path)
    pd.testing.assert_frame_equal(df, out)


def test_json_round_trip(tmp_path) -> None:
    obj = {"a": 1, "b": [1, 2]}
    path = tmp_path / "test.json"
    write_json(obj, path)
    assert read_json(path) == obj
