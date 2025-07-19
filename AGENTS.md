# AGENT REGELN

ZIELDATEI: ZIEL-AGENTS.md
BACKLOG: OFFEN.md
ERLEDIGT: erledigt.txt
FORTSCHRITT: fortschritt.txt

PRINZIP:
1. Wähle IMMER genau EIN kleinstes noch offenes Item (ID).
2. Implementiere nur dessen Änderung(en).
3. Fülle/ersetze alle zugehörigen Platzhalter im Code ( // TODO:<ID> ... ).
4. Führe (falls vorhanden) passende Tests aus oder lege Minimaltest an.
5. Aktualisiere:
   - erledigt.txt (ID + Kurzbeschreibung + Datum)
   - OFFEN.md (streiche oder markiere ID als DONE)
   - fortschritt.txt (Prozent neu berechnen)
6. Commit-Message: `<ID> <kurz>` – nur diese Änderung.
7. Keine neuen Features anlegen bevor alle Basis IDs der aktuellen Phase fertig.
8. Bei Blockade: Erzeuge Kommentar in OFFEN.md unter BLOCKIERT mit Grund + nächster Versuchsschritt.

PROGRESS-BERECHNUNG:
Prozent = (Anzahl erledigt BASIS-Tasks / Gesamt BASIS-Tasks) * 100, ohne Stretch.

TASK-FORMAT in OFFEN.md:
`- [ ] <ID> <Kurztitel> :: Ziel :: Akzeptanz`
Nur eine eindeutig prüfbare Aktion pro ID.

KEINE zusammengefassten Multi-Schritte in einer ID.

ABBRUCHKRITERIEN FÜR EINEN TASK:
Alle Akzeptanzpunkte erfüllt, Platzhalter entfernt, Code kompiliert/startet.

QUALITY CHECKLIST JE COMMIT:
- Nur Files dieses Tasks geändert?
- Platzhalter des Tasks entfernt/ersetzt?
- Lint/Format (ruff oder black) sauber?
- Test / manuelle Mini-Prüfung durchgeführt?

