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
# Build an AppImage for ModulTool using PyInstaller.
# Requires: pyinstaller, appimagetool
set -e
APP=ModulTool
VERSION=${1:-0.1.0}
WORK=build/appimage
rm -rf "$WORK"
mkdir -p "$WORK/AppDir/usr/bin"
pyinstaller --noconfirm --windowed --name "$APP" app.py
cp dist/$APP/$APP "$WORK/AppDir/usr/bin/"
cat > "$WORK/AppDir/$APP.desktop" <<DESK
[Desktop Entry]
Name=$APP
Exec=$APP
Icon=$APP
Type=Application
Categories=Utility;
DESK
cp modultool/icon.png "$WORK/AppDir/$APP.png" 2>/dev/null || touch "$WORK/AppDir/$APP.png"
appimagetool "$WORK/AppDir" "$WORK/$APP-$VERSION.AppImage"
echo "AppImage created at $WORK/$APP-$VERSION.AppImage"
