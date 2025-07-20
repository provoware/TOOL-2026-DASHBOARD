#!/usr/bin/env bash
# Setup-Skript fuer ModulTool
# Erstellt eine virtuelle Umgebung und installiert die Abhaengigkeiten.

set -e

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo "Setup abgeschlossen. Starte mit 'source .venv/bin/activate' und 'python app.py'"
