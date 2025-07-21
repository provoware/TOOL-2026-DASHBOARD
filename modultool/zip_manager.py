import shutil
from datetime import datetime
from pathlib import Path
from zipfile import ZipFile

from .config import get_data_dir, get_root_dir
from .logger import logger


class ZipManager:
    """Export and import the data directory as a zip archive."""

    def export_zip(self, dest: Path | None = None) -> Path:
        data_dir = get_data_dir()
        exports_dir = get_root_dir() / "exports"
        exports_dir.mkdir(exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dest = dest or exports_dir / f"data_{stamp}.zip"
        with ZipFile(dest, "w") as zf:
            for path in data_dir.rglob("*"):
                if path.is_file():
                    zf.write(path, path.relative_to(data_dir))
        logger.info("export zip created: %s", dest.name)
        return dest

    def import_zip(self, zip_path: Path) -> None:
        data_dir = get_data_dir()
        if data_dir.exists():
            shutil.rmtree(data_dir)
        with ZipFile(zip_path, "r") as zf:
            zf.extractall(data_dir)
        logger.info("import zip restored from: %s", zip_path.name)


zip_manager = ZipManager()


if __name__ == "__main__":
    import sys

    action = sys.argv[1] if len(sys.argv) > 1 else "export"
    file_arg = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    if action == "export":
        result = zip_manager.export_zip(file_arg)
        print(result)
    elif action == "import" and file_arg:
        zip_manager.import_zip(file_arg)
    else:
        print(
            "Usage: python -m modultool.zip_manager [export [dest.zip]|import <src.zip>]"
        )
