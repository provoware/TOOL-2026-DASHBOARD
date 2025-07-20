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
