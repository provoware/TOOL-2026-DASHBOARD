from __future__ import annotations


class UndoRedoManager:
    """Track history for undo and redo with limited depth."""

    def __init__(self, depth: int = 2) -> None:
        self.depth = depth
        self._undo: list[list[str]] = []
        self._redo: list[list[str]] = []

    def record(self, state: list[str]) -> None:
        """Store a copy of the current state for undo."""
        self._undo.append(list(state))
        if len(self._undo) > self.depth:
            self._undo.pop(0)
        self._redo.clear()

    def undo(self, current_state: list[str]) -> list[str]:
        """Return previous state if available."""
        if not self._undo:
            return current_state
        self._redo.append(list(current_state))
        if len(self._redo) > self.depth:
            self._redo.pop(0)
        return self._undo.pop()

    def redo(self, current_state: list[str]) -> list[str]:
        """Return next state if available."""
        if not self._redo:
            return current_state
        self._undo.append(list(current_state))
        if len(self._undo) > self.depth:
            self._undo.pop(0)
        return self._redo.pop()
