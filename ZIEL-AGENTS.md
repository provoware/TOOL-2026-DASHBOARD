in bilddatei ist das Ziellayout als Orientierung enthalten. LAYOUT-ZIEL.png
# HAUPTZIEL
Modular erweiterbares Desktop-Tool (Python + PySide6) mit 3-Spalten-Dashboard, Autosave, Backups, Selbstheilung, barrierefähigem Theme-System, Dummy-Daten, stabil offline, kein harter Absturz.

# ERFOLGSKRITERIEN (MVP)
- Start ohne Fehler offline (Dummy-Daten erzeugt).
- Dashboard mit 3x3 Karten + Seitenleisten sichtbar.
- Mindestens 1 Beispielmodul (Genre) voll ladbar, speichert JSON, Autosave aktiv.
- Backup/Restore Knopf funktioniert (ein Backup-Verzeichnis angelegt + Wiederherstellung testbar).
- Fehler bei fehlender Datei erzeugt Dummy ohne Absturz.
- HighContrast Theme umschaltbar.
- Hilfe-Tooltip zu mindestens 1 UI-Element.
- Test-Suite führt Kern-Tests (Loader, Autosave) fehlerfrei aus.

# NON-ZIELE (SPÄTER)
Marketplace, Sandbox Subprozess, Internationalisierung, Telemetrie extern, Flatpak.

# FERTIG DEFINIERT WENN
Alle MVP-Kriterien erfüllt + Selfcheck ohne kritische Fehler + README mit Install + Modul-Hinzufügen-Anleitung vorhanden.
