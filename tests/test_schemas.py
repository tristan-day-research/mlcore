from mlcore import DataBatch, ModelCard


def test_modelcard_serializes() -> None:
    card = ModelCard(name="m", version="1")
    data = card.as_dict()
    assert data["name"] == "m"
    assert data["version"] == "1"


def test_databatch_serializes() -> None:
    batch = DataBatch(n_rows=10, schema_version="v1")
    assert batch.as_dict()["n_rows"] == 10
