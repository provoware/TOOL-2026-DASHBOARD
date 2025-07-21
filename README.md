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
* **Selfcheck starten** (kurzer Testlauf):
  ```bash
  python -m modultool.selfcheck
  ```
  Das Skript erstellt fehlende Dummy-Daten und schreibt eine Meldung ins Log.
  Im Programm selbst wird alle 60 Minuten automatisch ein Selfcheck ausgeführt.
* **Sidebar testen** (linke Navigationsleiste):
  ```bash
  python app.py
  ```
  Klicke auf die Knöpfe "Nav 1" bis "Nav 3". In der Logdatei siehst du dann den Eintrag "Nav 1 clicked" usw.

* **Reset auf Werkzustand** ("factory reset" – stellt Standarddateien wieder her):
  ```bash
  python -m modultool.reset_manager
  ```
  Dadurch werden eigene Daten gelöscht und die Standardwerte über `selfcheck` neu angelegt.
* **Daten exportieren** (komplette Sicherung als ZIP):
  ```bash
  python -m modultool.zip_manager export
  ```
  Die ZIP-Datei erscheint im Ordner `exports/`. Ein eigener Dateiname ist optional möglich.
* **Daten importieren** (gesicherte ZIP wiederherstellen):
  ```bash
  python -m modultool.zip_manager import exports/data_YYYYMMDD_HHMMSS.zip
  ```
  Dabei werden bestehende Daten ersetzt.
* **Letzte Änderungen rückgängig machen** ("Undo" – vorherigen Zustand wiederherstellen):
  ```bash
  python - <<'PY'
  from modultool.modules import GenresModule
  module = GenresModule()
  module.add_genre("Rock")
  module.undo()
  PY
  ```
  Mit `module.redo()` kannst du den Schritt erneut anwenden.
