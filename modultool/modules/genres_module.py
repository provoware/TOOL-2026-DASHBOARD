import json
from pathlib import Path

from .base_module import BaseModule
from ..autosave import autosave
from ..config import get_defaults_dir
from ..error_handler import load_json


class GenresModule(BaseModule):
    """Simple module to manage music genres."""

    name = "genres"

    def __init__(self, path: Path | None = None):
        super().__init__()
        self.file = path or get_defaults_dir() / "genres.json"
        self.genres = load_json(self.file, [])

    def add_genre(self, genre: str) -> None:
        """Add a genre to the internal list."""
        self.genres.append(genre)
        autosave.autosave(self)

    def save(self) -> None:
        """Write genres to disk."""
        with self.file.open("w", encoding="utf-8") as f:
            json.dump(self.genres, f, indent=2, ensure_ascii=False)

    def get_genres(self) -> list[str]:
        """Return the list of genres."""
        return list(self.genres)
