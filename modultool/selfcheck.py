import json

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
