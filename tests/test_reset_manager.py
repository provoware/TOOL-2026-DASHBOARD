import json
import importlib

from modultool import config, reset_manager, selfcheck


def test_reset_recreates_defaults(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    defaults_dir = data_dir / "defaults"
    defaults_dir.mkdir(parents=True)
    themes_dir = data_dir / "themes"
    themes_dir.mkdir()

    (data_dir / "module_order.json").write_text("[]", encoding="utf-8")
    genres_file = defaults_dir / "genres.json"
    genres_file.write_text(json.dumps(["Custom"]), encoding="utf-8")

    monkeypatch.setattr(config, "get_data_dir", lambda: data_dir)
    monkeypatch.setattr(selfcheck, "get_defaults_dir", lambda: defaults_dir)

    importlib.reload(reset_manager)

    reset_manager.reset_manager.reset()

    assert not (data_dir / "module_order.json").exists()
    with genres_file.open(encoding="utf-8") as f:
        genres = json.load(f)
    assert genres == selfcheck.DEFAULT_GENRES
