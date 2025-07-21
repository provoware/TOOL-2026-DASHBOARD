import importlib

from modultool import config


def test_export_import_zip(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    sample = data_dir / "sample.txt"
    sample.write_text("hello", encoding="utf-8")

    monkeypatch.setattr(config, "get_data_dir", lambda: data_dir)
    monkeypatch.setattr(config, "get_root_dir", lambda: tmp_path)

    module = importlib.import_module("modultool.zip_manager")
    importlib.reload(module)

    dest = module.zip_manager.export_zip()
    sample.unlink()

    module.zip_manager.import_zip(dest)
    assert (data_dir / "sample.txt").read_text(encoding="utf-8") == "hello"
