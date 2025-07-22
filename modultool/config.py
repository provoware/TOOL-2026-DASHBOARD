from __future__ import annotations

from pathlib import Path
import os
import tempfile

APP_VERSION = "0.1.0"

# sandbox directory used when sandbox mode is active
_SANDBOX_DIR: Path | None = None


def enable_sandbox(tmp_dir: Path | None = None) -> Path:
    """Activate sandbox mode and return the directory in use."""
    global _SANDBOX_DIR
    if tmp_dir is None:
        tmp_dir = Path(tempfile.mkdtemp(prefix="modultool_sandbox_"))
    _SANDBOX_DIR = Path(tmp_dir)
    return _SANDBOX_DIR


def disable_sandbox() -> None:
    """Disable sandbox mode."""
    global _SANDBOX_DIR
    _SANDBOX_DIR = None


def is_sandbox() -> bool:
    """Return True if sandbox mode is active."""
    return _SANDBOX_DIR is not None


def get_root_dir() -> Path:
    """Return repository root directory or sandbox directory."""
    if _SANDBOX_DIR is not None:
        return _SANDBOX_DIR
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


# auto-enable sandbox if environment variable is set
if os.getenv("MODULTOOL_SANDBOX"):
    enable_sandbox()
