from pathlib import Path

from mlcore import AppSettings


def test_settings_from_env(tmp_path, monkeypatch) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text("ENV=prod\nDATA_DIR=/tmp/data\nS3_BUCKET=my-bucket\n")
    monkeypatch.chdir(tmp_path)
    settings = AppSettings.from_env()
    assert settings.env == "prod"
    assert settings.data_dir == Path("/tmp/data")
    assert settings.s3_bucket == "my-bucket"
