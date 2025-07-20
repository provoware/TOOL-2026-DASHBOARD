# modern-tool

Dies ist ein kleines Beispielprojekt. Ziel ist eine modulare Desktop-Anwendung.

## Schnellstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Tests führst du so aus:

```bash
pytest -q
```

Die Logdatei findest du im Ordner `logs/modultool.log`.

Alle wichtigen Pfade liegen zentral in `modultool/config.py`. Dort steht auch die
aktuelle Versionsnummer (`APP_VERSION`).

## Dummy-Daten

Im Verzeichnis `data/defaults` liegen Beispielinhalte. Damit startet das Programm
nie leer. Die Dateien `genres.json` und `quotes.json` kannst du nach Belieben
anpassen. Sie sind im **JSON-Format** (Textdatei mit strukturierten Daten). Ein
eigenes Genre fügst du so hinzu:

```bash
echo '  "Metal"' >> data/defaults/genres.json
```

## Weiterführende Tipps

* **Virtuelle Umgebung** ("virtual environment" – abgeschottete Python-Umgebung)
  anlegen:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
* **Abhängigkeiten** (nötige Bibliotheken) installieren:
  ```bash
  pip install -r requirements.txt
  ```
* **Tests ausführen**:
  ```bash
  pytest -q | tee last_test.log
  ```
