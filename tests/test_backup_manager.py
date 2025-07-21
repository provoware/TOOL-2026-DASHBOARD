import importlib
from pathlib import Path

from modultool import config


def test_create_backup(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    sample = data_dir / "sample.txt"
    sample.write_text("hello", encoding="utf-8")

    monkeypatch.setattr(config, "get_data_dir", lambda: data_dir)
    monkeypatch.setattr(config, "get_root_dir", lambda: tmp_path)

    backup_module = importlib.import_module("modultool.backup")
    importlib.reload(backup_module)

    dest = backup_module.backup.create_backup()
    copied = dest / "sample.txt"
    assert copied.read_text(encoding="utf-8") == "hello"
