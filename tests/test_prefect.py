from mlcore.integrations.prefect.tasks import flow_default, task_default


def test_prefect_wrappers() -> None:
    @task_default()
    def add(x: int, y: int) -> int:
        return x + y

    @flow_default
    def pipeline() -> int:
        return add(1, 2)

    assert pipeline() == 3
