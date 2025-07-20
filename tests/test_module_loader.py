from modultool import module_loader


def test_discover_modules_returns_genres():
    modules = module_loader.discover_modules()
    assert "GenresModule" in modules
