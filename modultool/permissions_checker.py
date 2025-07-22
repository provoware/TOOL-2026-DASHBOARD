import json
from pathlib import Path

from .logger import logger
from .config import get_root_dir

ALLOWED_PERMISSIONS = {"read", "write", "network"}


def check_manifest(manifest_path: Path | None = None) -> bool:
    """Validate permissions in the manifest file."""
    if manifest_path is None:
        manifest_path = get_root_dir() / "manifest.json"

    if not manifest_path.exists():
        logger.error("manifest fehlt: %s", manifest_path)
        return False

    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        logger.error("manifest unlesbar: %s", exc)
        return False

    perms = data.get("permissions", [])
    invalid = [p for p in perms if p not in ALLOWED_PERMISSIONS]
    if invalid:
        logger.error("unbekannte Berechtigungen: %s", ", ".join(invalid))
        return False

    logger.info("permissions ok: %s", ", ".join(perms))
    return True


if __name__ == "__main__":  # pragma: no cover - cli usage
    ok = check_manifest()
    print("Manifest OK" if ok else "Manifest fehlerhaft")
