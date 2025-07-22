from modultool import module_loader


def test_discover_modules_returns_genres():
    modules = module_loader.discover_modules()
    assert "GenresModule" in modules


def test_discover_modules_handles_import_error(monkeypatch):
    orig_iter = module_loader.pkgutil.iter_modules

    def fake_iter_modules(path):
        yield from orig_iter(path)

        class Info:
            name = "broken"

        yield Info()

    monkeypatch.setattr(module_loader.pkgutil, "iter_modules", fake_iter_modules)

    orig_import = module_loader.importlib.import_module

    def fake_import(name, package=None):
        if name == "modultool.modules.broken":
            raise RuntimeError("boom")
        return orig_import(name, package=package)

    monkeypatch.setattr(module_loader.importlib, "import_module", fake_import)

    modules = module_loader.discover_modules()
    placeholder = modules.get("broken")
    assert placeholder is not None
    inst = placeholder()
    assert hasattr(inst, "error") and "boom" in inst.error
