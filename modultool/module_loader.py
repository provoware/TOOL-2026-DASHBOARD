import importlib
import pkgutil

from .modules import BaseModule


def discover_modules() -> dict[str, type[BaseModule]]:
    """Discover and return available module classes."""
    modules: dict[str, type[BaseModule]] = {}
    package = importlib.import_module("modultool.modules")
    for info in pkgutil.iter_modules(package.__path__):
        if info.name == "base_module":
            continue
        module = importlib.import_module(f"modultool.modules.{info.name}")
        for attr in dir(module):
            obj = getattr(module, attr)
            if (
                isinstance(obj, type)
                and issubclass(obj, BaseModule)
                and obj is not BaseModule
            ):
                modules[obj.__name__] = obj
    return modules
