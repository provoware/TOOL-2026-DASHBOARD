#!/usr/bin/env bash
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
