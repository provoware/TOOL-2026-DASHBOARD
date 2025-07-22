import json
from pathlib import Path

import modultool.permissions_checker as pc


def test_check_manifest_ok(tmp_path, monkeypatch):
    manifest = tmp_path / "manifest.json"
    manifest.write_text(
        json.dumps({"permissions": ["read", "write"]}), encoding="utf-8"
    )
    monkeypatch.setattr(pc, "get_root_dir", lambda: tmp_path)
    assert pc.check_manifest()


def test_check_manifest_invalid(tmp_path, monkeypatch):
    manifest = tmp_path / "manifest.json"
    manifest.write_text(
        json.dumps({"permissions": ["delete"]}), encoding="utf-8"
    )
    monkeypatch.setattr(pc, "get_root_dir", lambda: tmp_path)
    assert not pc.check_manifest()
