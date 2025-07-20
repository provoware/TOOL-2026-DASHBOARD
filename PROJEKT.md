# Projekt Übersicht

Diese Datei sammelt in einfacher Sprache alle wichtigen Infos zum **ModulTool**.

## Bisher umgesetzt

- Grundstruktur des Repositories mit Dokumenten.
- Grund-Ordnergerüst (`modultool`, `data`, `modules`, `tests`, `docs`, `scripts`).
- Detaillierte Zielbeschreibung in `ZIEL-AGENTS.md`.
- Erweiterte Planung in `ZIEL_UND_ERWEITERUNGS_AGENTS.md`.
- Minimales `requirements.txt` mit `pyside6` und `pytest` angelegt.

## Vollbeschreibung

Das Projekt soll ein leicht bedienbares Desktop‑Werkzeug werden, das viele Module (Bausteine) enthält. Jede Funktion arbeitet auch ohne Internet. Die Oberfläche folgt einem Drei‑Spalten‑Layout.

### Hauptmerkmale

1. **Autosave** (Automatisches Speichern): Alle Eingaben werden regelmäßig gesichert, damit nichts verloren geht.
2. **Backup** (Sicherheitskopie): Es gibt einen Knopf, der alle Daten in einem separaten Ordner sichert.
3. **Theme-System** (Erscheinungsbild): Farben und Kontraste lassen sich umschalten, damit die Bedienung barrierefrei wird.
4. **Module** (Erweiterungen): Funktionen wie Genre-Verwaltung, Song‑Editor oder Mindmap können als Module geladen werden.
5. **Datei-Router** (FileRouter): Dateien werden nach Typ sortiert abgelegt, z.B. Audio unter `audio/YYYY-MM-DD/`.

Weitere Details stehen in den Ziel-Dateien. Dort ist die komplette Roadmap (Zeitplan) beschrieben.

## Laien-Tipps

Die folgenden Schritte zeigen, wie man das Projekt lokal ausprobiert. Alle Befehle (Kommandos) bitte in einer Konsole eingeben.

1. **Repository klonen** (Kopie holen)

   ```bash
   git clone <REPO-URL>
   cd modern-tool
   ```

2. **Virtuelle Umgebung** (abgeschottete Python-Installation) erstellen und aktivieren

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Abhängigkeiten installieren** (benötigte Pakete)

   ```bash
   pip install -r requirements.txt
   ```

4. **Tests ausführen** (Prüfung)

   ```bash
   pytest -q
   ```

5. **Programm starten** (falls vorhanden)

   ```bash
   python app.py
   ```

Damit sollte ein leeres Fenster erscheinen. Weitere Module folgen Schritt für Schritt.

## Weiterführende Tipps

* **Ordner prüfen**: Mit `ls -R` (Inhalt auflisten) sieht man das gesamte Projektgerüst.
* **Pip aktualisieren** (Paketverwaltung):

  ```bash
  python -m pip install --upgrade pip
  ```

* **Virtuelle Umgebung verlassen**:

  ```bash
  deactivate
  ```

* **Installierte Pakete prüfen** (Kontrolle):

  ```bash
  pip list
  ```

Diese einfachen Befehle helfen beim Einstieg und bei einer sauberen Umgebung.

