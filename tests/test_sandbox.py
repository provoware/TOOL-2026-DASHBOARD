from modultool import config


def test_enable_sandbox(tmp_path):
    orig = config.get_root_dir()
    config.enable_sandbox(tmp_path)
    assert config.is_sandbox() is True
    assert config.get_root_dir() == tmp_path
    config.disable_sandbox()
    assert config.is_sandbox() is False
    assert config.get_root_dir() == orig
