from pathlib import Path
from modultool import config


def test_version_constant():
    assert config.APP_VERSION == "0.1.0"


def test_path_functions():
    root = Path(__file__).resolve().parent.parent
    assert config.get_root_dir() == root
    assert config.get_data_dir() == root / "data"
    assert config.get_defaults_dir() == root / "data" / "defaults"
    assert config.get_log_dir() == root / "logs"
