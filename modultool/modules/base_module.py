from ..event_bus import event_bus


class BaseModule:
    """Base class for application modules."""

    name = "base"

    def __init__(self) -> None:
        event_bus.emit("module.open", self.name)

    def get_name(self) -> str:
        """Return the name of the module."""
        return self.name

    def start(self) -> None:
        """Optional hook to run when the module is loaded."""
        raise NotImplementedError
