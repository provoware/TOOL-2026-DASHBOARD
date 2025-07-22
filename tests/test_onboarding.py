import os
from PySide6.QtWidgets import QApplication, QDialog

from modultool.onboarding import create_onboarding


def test_create_onboarding_dialog():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    dlg = create_onboarding()
    assert isinstance(dlg, QDialog)
    assert dlg.objectName() == "onboarding"
    app.quit()
