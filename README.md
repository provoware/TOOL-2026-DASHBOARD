# VideoBatchTool

Dieses kleine Tool kombiniert Bilder und Audios zu MP4-Videos. 

## Schnellstart
```
python3 videobatch_launcher.py
```
Das Launcher-Skript richtet automatisch eine Python-Umgebung ein und startet die grafische Oberfläche.

## Bedienung in Kurzform
1. Bilder und Audios per Drag & Drop oder über die Schaltflächen laden.
2. Mit **Auto-Paaren** passende Dateien zuordnen.
3. Einstellungen prüfen (Zielordner, Qualität usw.).
4. Auf **START** klicken und warten.

Fertige Videos landen im gewählten Ausgabeverzeichnis. Verarbeitete Originale werden in den Ordner `benutzte_dateien` verschoben.

## Tipps für Einsteiger
- Die wichtigsten Befehle lassen sich über die Menüs oder Tastenkürzel bedienen.
- Unter *Ansicht → Farbschema* kann zwischen hellem, dunklem und kontrastreichem Design gewechselt werden.
- Sollte etwas nicht funktionieren, hilft ein Blick in die Logdatei über *Hilfe → Logdatei öffnen*.

## Weiterführende Tipps (für Laien)
- **Programme starten**: `python3 videobatch_launcher.py` richtet alles ein und öffnet die grafische Oberfläche (GUI). Zum direkten Testen kann `python3 videobatch_gui.py` verwendet werden.
- **Befehle im Terminal (Konsole)**:
  - Videos ohne GUI erstellen:
    ```
    python3 videobatch_extra.py --img bild1.jpg bild2.jpg --aud ton1.mp3 ton2.mp3 --out ausgabe_ordner
    ```
    Dabei steht `--img` für die Bilder, `--aud` für die Audios und `--out` für den Zielordner.
  - Selbsttest ausführen:
    ```
    python3 videobatch_extra.py --selftest
    ```
    So wird geprüft, ob alles korrekt funktioniert.
- **Schrift anpassen**: Über *Ansicht* lassen sich mit "Schrift +" oder "Schrift -" die Texte vergrößern bzw. verkleinern.
- **Kurzanleitung**: *Hilfe → Kurzanleitung* zeigt eine kurze Erläuterung aller Schritte.
