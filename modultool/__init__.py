from .logger import logger
from .selfcheck import run_selfcheck
from .help_engine import register_help
from .error_dialog import create_error_dialog
from .event_bus import event_bus
from .stats import stats
from .onboarding import show_onboarding

run_selfcheck()

__all__ = [
    "logger",
    "run_selfcheck",
    "register_help",
    "create_error_dialog",
    "event_bus",
    "stats",
    "show_onboarding",
]
