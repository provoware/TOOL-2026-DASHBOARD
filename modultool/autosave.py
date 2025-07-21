from __future__ import annotations

from .logger import logger


class AutosaveManager:
    """Minimal manager to persist module data immediately."""

    def autosave(self, module) -> None:
        if hasattr(module, "save"):
            module.save()
            logger.info(
                "autosave: %s saved", getattr(module, "name", module.__class__.__name__)
            )


autosave = AutosaveManager()
