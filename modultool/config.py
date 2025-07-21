from pathlib import Path

APP_VERSION = "0.1.0"


def get_root_dir() -> Path:
    """Return repository root directory."""
    return Path(__file__).resolve().parent.parent


def get_data_dir() -> Path:
    """Return the data directory inside the project."""
    return get_root_dir() / "data"


def get_defaults_dir() -> Path:
    """Return directory for default data files."""
    return get_data_dir() / "defaults"


def get_theme_dir() -> Path:
    """Return directory containing theme stylesheets."""
    return get_data_dir() / "themes"


def get_log_dir() -> Path:
    """Return directory for log files."""
    return get_root_dir() / "logs"
