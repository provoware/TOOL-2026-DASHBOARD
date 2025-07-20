from modultool.modules import BaseModule


def test_base_module_instantiation():
    module = BaseModule()
    assert module.get_name() == "base"
