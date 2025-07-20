import json

from modultool.modules import GenresModule


def test_add_genre(tmp_path):
    genres_file = tmp_path / "genres.json"
    genres_file.write_text(json.dumps(["Pop"]), encoding="utf-8")
    module = GenresModule(path=genres_file)
    module.add_genre("Electro")
    assert "Electro" in module.get_genres()
