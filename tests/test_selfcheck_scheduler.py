import time
import modultool.selfcheck as selfcheck


def test_scheduler_runs(monkeypatch):
    called = []
    monkeypatch.setattr(selfcheck, "run_selfcheck", lambda: called.append(True))
    scheduler = selfcheck.SelfcheckScheduler(interval=0.01)
    scheduler.start()
    time.sleep(0.03)
    scheduler.stop()
    assert called
