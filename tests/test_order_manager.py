import json

from modultool.order_manager import OrderManager


def test_move_persists_order(tmp_path):
    order_file = tmp_path / "order.json"
    order_file.write_text(json.dumps(["A", "B", "C"]), encoding="utf-8")

    manager = OrderManager(path=order_file)
    manager.move("C", 0)

    with order_file.open(encoding="utf-8") as f:
        data = json.load(f)
    assert data == ["C", "A", "B"]


def test_load_creates_default(tmp_path):
    order_file = tmp_path / "order.json"
    manager = OrderManager(path=order_file)
    assert order_file.exists()
    assert manager.get_order() == []
