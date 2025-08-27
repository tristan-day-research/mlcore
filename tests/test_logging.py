from mlcore import get_logger


def test_get_logger_emits(caplog) -> None:
    logger = get_logger("mlcore-test")
    with caplog.at_level("INFO"):
        logger.info("hello")
    assert "hello" in caplog.text
