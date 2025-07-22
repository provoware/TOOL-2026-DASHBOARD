#!/usr/bin/env bash
# Build an AppImage for ModulTool
# Requires: pyinstaller, appimagetool
set -e

APP_NAME="ModulTool"

if ! command -v pyinstaller >/dev/null; then
    echo "pyinstaller not found. Installing..." >&2
    pip install pyinstaller
fi

if ! command -v appimagetool >/dev/null; then
    echo "appimagetool not found. Please install AppImageKit." >&2
    exit 1
fi

# Clean previous build
rm -rf build dist "$APP_NAME.AppDir"

# Create binary with PyInstaller
pyinstaller --noconfirm --windowed --name "$APP_NAME" app.py

# Prepare AppDir structure
mkdir -p "$APP_NAME.AppDir/usr/bin"
cp dist/$APP_NAME/$APP_NAME "$APP_NAME.AppDir/usr/bin/"
cp -r data modultool "$APP_NAME.AppDir/usr/bin/"

# Desktop entry for launcher
cat > "$APP_NAME.AppDir/$APP_NAME.desktop" <<DESKTOP
[Desktop Entry]
Name=$APP_NAME
Exec=$APP_NAME
Icon=$APP_NAME
Type=Application
Categories=Utility;
DESKTOP

# Build AppImage
appimagetool "$APP_NAME.AppDir"

echo "AppImage created."
