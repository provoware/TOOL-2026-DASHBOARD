# BACKLOG (OFFEN)
Legende: P0 = kritisch Basis, P1 = Aufbau, P2 = Komfort, S = Stretch
Format: - [ ] ID (Phase) Titel :: Ziel :: Akzeptanz

## P0 Bootstrap & Struktur
- [x] T01 (P0) Grund-Ordnergerüst anlegen :: Verzeichnisstruktur steht :: Alle Verzeichnisse vorhanden, leerer Startcommit
- [x] T02 (P0) pyproject/requirements minimal :: Basisabhängigkeiten festgelegt :: Datei vorhanden, enthält pyside6 + pytest
- [x] T03 (P0) setup.sh minimal :: Ein-Klick-Setup venv + install :: Ausführbar, erzeugt .venv, startet ohne Crash
- [x] T04 (P0) app.py Einstieg + leeres Fenster :: GUI startet :: Fenster-Titel 'ModulTool' erscheint
- [x] T05 (P0) logger.py Basis :: Einheitlicher Logger :: Logdatei erstellt + erste Zeile geschrieben
- [x] T06 (P0) config.py Konstanten :: Zentrale Pfade/Version :: Versionkonstante + Pfadfunktionen nutzbar
- [x] T07 (P0) dummy daten anlegen :: Nie leer Start :: data/defaults/*.json existieren (genres.json, quotes.json)
- [x] T08 (P0) bootstrap Selfcheck Stub :: Vorstart Prüfung :: Fehlende defaults werden erzeugt (Logeintrag)
- [x] T09 (P0) base_module.py Skeleton :: Module Vertrag :: Klasse BaseModule kompiliert
- [x] T10 (P0) genres_module Grund :: Erstes Modul UI + Add :: Genre hinzufügen erscheint in Liste
- [x] T11 (P0) module_loader Discovery :: Automatische Modul-Erkennung :: genres_module wird geladen ohne ImportError
- [x] T12 (P0) dashboard Grid Cards :: 3x3 Platzhalter sichtbar :: 9 Cards, Titel, Klick loggt Info
- [x] T13 (P0) sidebar Navigation :: Linke Leiste aktiv :: Buttons reagieren (Log)
- [x] T14 (P0) statusbar Basis :: Statuszeile zeigt Meldungen :: Nach Aktion Text aktualisiert
- [x] T15 (P0) autosave manager minimal :: Änderungen persistieren :: genres.json aktualisiert nach Add
- [x] T16 (P0) backup manager basic :: Manuelles Backup erstellt :: Backup-Verzeichnis mit Kopie
- [x] T17 (P0) error handler stub :: Abfangen FileNotFound :: Fehlende Datei => Dummy + Log INFO
- [x] T18 (P0) theme loader dark :: Stylesheet angewendet :: Hintergrundfarbe wechselt erkennb.
- [x] T19 (P0) help_engine stub :: Tooltip für 1 Button :: Hover zeigt Hilfetext
- [x] T20 (P0) tests basis :: pytest läuft grün :: test_loader + test_autosave bestehen

## P1 Robustheit & UX
- [x] T21 (P1) HighContrast Theme
- [x] T22 (P1) Maximieren/Restore Modul
- [x] T23 (P1) Drag&Drop Modulreihenfolge speichern
- [x] T24 (P1) Backup Auto-Rotation
- [x] T25 (P1) Fehlerdialog UI (Benutzertext + Details)
- [x] T26 (P1) Settings Panel (Theme, FontScale)
- [x] T27 (P1) EventBus implementieren
- [x] T28 (P1) Stats sammeln (module.open)
- [x] T29 (P1) Reset auf Werkzustand
- [x] T30 (P1) Selfcheck periodisch

## P2 Komfort
- [x] T31 (P2) Import/Export ZIP
- [x] T32 (P2) Undo/Redo Basis (Genres)
- [x] T33 (P2) Kontext-Hilfe Panel (F1)
- [x] T34 (P2) Platzhalterkarte bei Modulfehler
- [ ] T35 (P2) Onboarding Overlays

## S (Stretch)
- [ ] TS1 (S) Sandbox Mode
- [ ] TS2 (S) Manifest Permissions Prüfer
- [ ] TS3 (S) AppImage Build Script

## BLOCKIERT
*(leer – bei Blockade Eintrag: ID :: Grund :: geplanter Retry)*

## PLATZHALTER IM CODE
Suche nach:
- `// TODO:Txx`
- `# TODO:Txx`
- `<Txx_PLACEHOLDER>`
Diese müssen nach Fertigstellung der jeweiligen ID entfernt oder ersetzt sein.

## ABHÄNGIGKEITEN (Reihenfolge)
T01→T02→T03→T04
T04→T09→T10→T11
T05,T06 vor T15
T15 vor T16 (Backup braucht Daten)
T17 nach T08
T18 nach T04
T19 nach T04
T20 nach T11,T15

