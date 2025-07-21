import json
from modultool.event_bus import event_bus
from modultool.stats import StatsManager


def test_stats_manager_records_module_open(tmp_path):
    path = tmp_path / "stats.json"
    manager = StatsManager(path=path)
    event_bus.emit("module.open", "Demo")
    event_bus.emit("module.open", "Demo")
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["Demo"] == 2
    event_bus.unsubscribe("module.open", manager.record_open)
