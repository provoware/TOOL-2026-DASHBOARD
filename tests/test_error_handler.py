import json
from pathlib import Path

from modultool.error_handler import load_json
from modultool.logger import logger


def test_load_json_creates_default(tmp_path, monkeypatch):
    target = tmp_path / "missing.json"
    logs = []

    def fake_log(msg, *args):
        logs.append(msg % args)

    monkeypatch.setattr(logger, "info", fake_log)

    data = load_json(target, {"foo": 1})
    assert data == {"foo": 1}
    assert target.exists()
    with target.open(encoding="utf-8") as f:
        assert json.load(f) == {"foo": 1}
    assert any("created with default" in m for m in logs)
