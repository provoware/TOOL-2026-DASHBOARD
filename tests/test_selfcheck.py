import json

import modultool.selfcheck as selfcheck


def test_run_selfcheck_creates_defaults(tmp_path, monkeypatch):
    monkeypatch.setattr(selfcheck, "get_defaults_dir", lambda: tmp_path)
    genres = tmp_path / "genres.json"
    quotes = tmp_path / "quotes.json"

    selfcheck.run_selfcheck()

    assert genres.exists()
    assert quotes.exists()

    with genres.open(encoding="utf-8") as f:
        assert json.load(f)
    with quotes.open(encoding="utf-8") as f:
        assert json.load(f)
