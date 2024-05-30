from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

class KBjbcdn(QMainWindow):
    def initUI(self):
        self.setWindowTitle("Алканы")
        uic.loadUi("aaaaa.ui", self).show()
        self.setFixedSize(self.size())
        self.LoadFile()
        self.LoadAlkan(self.alkan)
        self.izomerButton.clicked.connect(self.GoTo3)
        self.returnOnFirst.clicked.connect(self.Return1)
        self.nameAlkan.setReadOnly(True)
        self.infaAlkan.setReadOnly(True)

if __name__ == "__main__":
    if hasattr(QtCore.Qt, "AA_EnableHighDpiScaling"):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, "AA_UseHighDpiPixmaps"):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    current_window = Beginning(Alkanes, AlkansTable)
    current_window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())