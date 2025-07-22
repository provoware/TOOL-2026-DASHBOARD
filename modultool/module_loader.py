import importlib
import pkgutil

from .modules import BaseModule
from .logger import logger


def _create_placeholder(name: str, exc: Exception) -> type[BaseModule]:
    """Return a placeholder module class describing the import error."""

    class Placeholder(BaseModule):
        """Dummy module used when a real one fails to import."""

        error = str(exc)

        def start(self) -> None:  # pragma: no cover - just logs
            logger.warning("placeholder for %s: %s", name, self.error)

    Placeholder.__name__ = f"{name}_placeholder"
    Placeholder.name = name
    return Placeholder


def discover_modules() -> dict[str, type[BaseModule]]:
    """Discover and return available module classes."""
    modules: dict[str, type[BaseModule]] = {}
    package = importlib.import_module("modultool.modules")
    for info in pkgutil.iter_modules(package.__path__):
        if info.name == "base_module":
            continue
        try:
            module = importlib.import_module(f"modultool.modules.{info.name}")
        except Exception as exc:  # broad so broken modules still listed
            modules[info.name] = _create_placeholder(info.name, exc)
            logger.error("failed to load module %s: %s", info.name, exc)
            continue
        for attr in dir(module):
            obj = getattr(module, attr)
            if (
                isinstance(obj, type)
                and issubclass(obj, BaseModule)
                and obj is not BaseModule
            ):
                modules[obj.__name__] = obj
    return modules
