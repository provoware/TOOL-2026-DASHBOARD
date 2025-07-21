from modultool.event_bus import EventBus


def test_subscribe_and_emit():
    bus = EventBus()
    received = []

    def handler(value):
        received.append(value)

    bus.subscribe("test", handler)
    bus.emit("test", 123)
    assert received == [123]


def test_unsubscribe():
    bus = EventBus()
    called = False

    def handler():
        nonlocal called
        called = True

    bus.subscribe("demo", handler)
    bus.unsubscribe("demo", handler)
    bus.emit("demo")
    assert called is False
