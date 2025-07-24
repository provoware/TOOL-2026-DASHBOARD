# Repository Guide

Dieses Projekt besteht aus drei Python-Skripten, die zusammen das "VideoBatchTool" bilden. Das Tool soll stabil, einfach bedienbar und barrierearm bleiben.

## Regeln fuer Aenderungen
- Nur die Dateien `videobatch_gui.py`, `videobatch_extra.py` und `videobatch_launcher.py` bearbeiten oder ergaenzen.
- Keine neuen Textdateien (README, TODO usw.) anlegen oder wiederherstellen.
- Hilfe-Texte in den Skripten in einfacher deutscher Sprache verfassen. Fachbegriffe in Klammern kurz erklaeren.
- Features so implementieren, dass sie auch fuer Anfaenger:innen und sehschwache Menschen gut nutzbar sind (z.B. Farbschema, grosse Schrift).

## Tests
Nach jeder Aenderung muss folgendes Kommando erfolgreich laufen:
```bash
python3 -m py_compile videobatch_extra.py videobatch_gui.py videobatch_launcher.py
```
Wenn Abhaengigkeiten fehlen, versuche sie mit `pip` oder `apt` zu installieren.

