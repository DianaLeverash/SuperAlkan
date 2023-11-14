from Второе_окно import Alkanes
from Первое_окно import Beginning
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
from Четвертое_окно import History


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    if hasattr(QtCore.Qt, "AA_EnableHighDpiScaling"):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, "AA_UseHighDpiPixmaps"):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    current_window = Beginning(Alkanes)
    current_window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())