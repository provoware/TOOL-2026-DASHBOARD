import json
from modultool.event_bus import event_bus
from modultool.stats import StatsManager


def test_stats_manager_records_module_open(tmp_path):
    path = tmp_path / "stats.json"
    manager = StatsManager(path=path)
    event_bus.emit("module.open", "Demo")
    event_bus.emit("module.open", "Demo")
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["modules"]["Demo"] == 2
    event_bus.unsubscribe("module.open", manager.record_open)
    event_bus.unsubscribe("error.occurred", manager.record_error)


def test_stats_manager_records_errors(tmp_path):
    path = tmp_path / "stats.json"
    manager = StatsManager(path=path)
    event_bus.emit("error.occurred")
    event_bus.emit("error.occurred")
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["errors"] == 2
    event_bus.unsubscribe("module.open", manager.record_open)
    event_bus.unsubscribe("error.occurred", manager.record_error)
