import json
import threading

from .config import get_defaults_dir
from .logger import logger

# Default content used when files are missing
DEFAULT_GENRES = ["Pop", "Rock", "Jazz", "Classical"]
DEFAULT_QUOTES = [
    {"text": "Keep it simple", "author": "Unknown"},
    {"text": "Less is more", "author": "Architect Ludwig Mies van der Rohe"},
]


def run_selfcheck() -> None:
    """Ensure required default data files exist."""
    defaults_dir = get_defaults_dir()
    defaults_dir.mkdir(parents=True, exist_ok=True)

    genres_file = defaults_dir / "genres.json"
    if not genres_file.exists():
        genres_file.write_text(
            json.dumps(DEFAULT_GENRES, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        logger.info("defaults: genres.json erzeugt")

    quotes_file = defaults_dir / "quotes.json"
    if not quotes_file.exists():
        quotes_file.write_text(
            json.dumps(DEFAULT_QUOTES, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        logger.info("defaults: quotes.json erzeugt")

    logger.info("Selfcheck abgeschlossen")


class SelfcheckScheduler:
    """Run selfcheck periodically in a background timer."""

    def __init__(self, interval: int = 3600) -> None:
        self.interval = interval
        self._timer: threading.Timer | None = None

    def start(self) -> None:
        """Begin periodic execution of ``run_selfcheck``."""
        self.stop()
        self._schedule()

    def _schedule(self) -> None:
        self._timer = threading.Timer(self.interval, self._run)
        self._timer.daemon = True
        self._timer.start()

    def _run(self) -> None:
        run_selfcheck()
        self._schedule()

    def stop(self) -> None:
        """Cancel the periodic execution."""
        if self._timer:
            self._timer.cancel()
            self._timer = None


selfcheck_scheduler = SelfcheckScheduler()
