from pathlib import Path
import json


def test_default_data_files_exist():
    root = Path(__file__).resolve().parent.parent
    defaults_dir = root / "data" / "defaults"
    genres_file = defaults_dir / "genres.json"
    quotes_file = defaults_dir / "quotes.json"

    assert genres_file.exists(), "genres.json fehlt"
    assert quotes_file.exists(), "quotes.json fehlt"

    # Ensure files contain valid JSON
    with genres_file.open(encoding="utf-8") as f:
        genres = json.load(f)
    with quotes_file.open(encoding="utf-8") as f:
        quotes = json.load(f)

    assert (
        isinstance(genres, list) and genres
    ), "genres.json sollte eine Liste enthalten"
    assert (
        isinstance(quotes, list) and quotes
    ), "quotes.json sollte eine Liste enthalten"
