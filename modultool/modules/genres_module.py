import json
from pathlib import Path

from .base_module import BaseModule
from ..config import get_defaults_dir


class GenresModule(BaseModule):
    """Simple module to manage music genres."""

    name = "genres"

    def __init__(self, path: Path | None = None):
        self.file = path or get_defaults_dir() / "genres.json"
        if self.file.exists():
            with self.file.open(encoding="utf-8") as f:
                self.genres = json.load(f)
        else:
            self.genres = []

    def add_genre(self, genre: str) -> None:
        """Add a genre to the internal list."""
        self.genres.append(genre)

    def get_genres(self) -> list[str]:
        """Return the list of genres."""
        return list(self.genres)
