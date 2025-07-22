import os


def test_build_script_exists():
    path = os.path.join("scripts", "build_appimage.sh")
    assert os.path.isfile(path), "build script missing"
    with open(path, "r", encoding="utf-8") as f:
        first_line = f.readline().strip()
    assert first_line.startswith("#!/usr/bin/env bash")
