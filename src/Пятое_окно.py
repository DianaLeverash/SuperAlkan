from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget

class AlkansTable(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon(r'C:\Users\Diana\Desktop\Алканы PyQT\Проект Алканы\src\иконка.jpg'))

    def initUI(self):
        self.setWindowTitle('Таблица всех алканов')
        uic.loadUi('Алканы и изомеры 5.ui', self)
        self.setFixedSize(self.size())
