from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from typing import Any


class EventBus:
    """Simple publish/subscribe event system."""

    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[..., Any]]] = defaultdict(list)

    def subscribe(self, event: str, callback: Callable[..., Any]) -> None:
        """Register callback for an event."""
        self._subscribers[event].append(callback)

    def unsubscribe(self, event: str, callback: Callable[..., Any]) -> None:
        """Remove callback for an event if present."""
        if callback in self._subscribers.get(event, []):
            self._subscribers[event].remove(callback)

    def emit(self, event: str, *args: Any, **kwargs: Any) -> None:
        """Send event to all registered listeners."""
        for callback in list(self._subscribers.get(event, [])):
            callback(*args, **kwargs)


# Global instance used by the application
event_bus = EventBus()
