class BaseModule:
    """Base class for application modules."""

    name = "base"

    def get_name(self) -> str:
        """Return the name of the module."""
        return self.name

    def start(self) -> None:
        """Optional hook to run when the module is loaded."""
        raise NotImplementedError
