import os
import importlib
import sys
import logging


def test_log_file_created(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    if root not in sys.path:
        sys.path.insert(0, root)
    module = importlib.import_module("modultool.logger")
    module.logger.info("Testeintrag")
    logging.shutdown()
    log_file = module.LOG_FILE
    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert "Logger initialisiert" in content.splitlines()[0]
    module = importlib.import_module("modultool.logger")
    module.logger.info("Testeintrag")
    logging.shutdown()
    log_file = module.LOG_FILE
    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert "Logger initialisiert" in content.splitlines()[0]
