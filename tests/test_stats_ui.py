import importlib
import os

from PySide6.QtWidgets import QApplication

from modultool.event_bus import event_bus
from modultool.stats import StatsManager


def test_stats_labels_update(tmp_path, monkeypatch):
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

    manager = StatsManager(path=tmp_path / "stats.json")
    import importlib
    stats_module = importlib.import_module("modultool.stats")



    monkeypatch.setattr(stats_module, "stats", manager)

    app_module = importlib.import_module("app")
    importlib.reload(app_module)
    monkeypatch.setattr(app_module, "stats", manager)

    app = QApplication.instance() or QApplication([])
    window = app_module.MainWindow()

    event_bus.emit("module.open", "Demo")
    event_bus.emit("error.occurred")

    assert window.error_label.text() == "Fehler: 1"
    assert window.module_label.text() == "Beliebtestes Modul: Demo"

    window.close()
    app.quit()
    event_bus.unsubscribe("module.open", manager.record_open)
    event_bus.unsubscribe("error.occurred", manager.record_error)
