from __future__ import annotations

from pathlib import Path
import re


def _hex_to_luminance(hex_color: str) -> float:
    r, g, b = [int(hex_color[i : i + 2], 16) / 255 for i in (0, 2, 4)]

    def channel(c: float) -> float:
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(r), channel(g), channel(b))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _contrast_ratio(bg: str, fg: str) -> float:
    l1 = _hex_to_luminance(bg)
    l2 = _hex_to_luminance(fg)
    if l1 < l2:
        l1, l2 = l2, l1
    return (l1 + 0.05) / (l2 + 0.05)


def _check_file(path: Path) -> None:
    style = path.read_text(encoding="utf-8")
    match = re.search(
        r"background-color:\s*#([0-9a-fA-F]{6}).*?color:\s*#([0-9a-fA-F]{6})",
        style,
        re.DOTALL,
    )
    if match:
        ratio = _contrast_ratio(match.group(1), match.group(2))
        print(f"{path.name}: {ratio:.2f}:1")
        if ratio < 4.5:
            print("  Warnung: Kontrast unter 4.5:1")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    dirs = [root / "data" / "themes", Path.home() / ".modultool" / "themes"]
    for d in dirs:
        if not d.exists():
            continue
        for file in d.glob("*.qss"):
            _check_file(file)


if __name__ == "__main__":
    main()
