from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow


class Izomers(QMainWindow):
    def __init__(self, Class1, Class2, alkan):
        self.Class1 = Class1
        self.Class2 = Class2
        self.alkan = alkan
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon(r'C:\Users\Diana\Desktop\Алканы PyQT\Проект Алканы\src\иконка.jpg'))

    def initUI(self):
        self.setWindowTitle('Изомеры')
        self.slovar = {}
        uic.loadUi('Алканы и изомеры 3.ui', self)
        self.setFixedSize(self.size())
        self.LoadFile()
        self.LoadAlkan(self.alkan)
        self.returnOnSecond.clicked.connect(self.Return2)
        self.infaIzomer.setReadOnly(True)
        self.textEdit_2.setReadOnly(True)
        self.nameAlkan.setReadOnly(True)

    def LoadFile(self):
        from slovar import LoadFiles
        self.slovar = LoadFiles()

    def LoadAlkan(self, alkan_name):
        self.nameAlkan.setText("Изомеры " + alkan_name)
        stroka = ""
        for elem in self.slovar[alkan_name.lower()][1]:
            stroka += elem
        self.infaIzomer.setText(stroka)

    def Return2(self):
        self.second_window = self.Class2(self.Class1, Izomers, self.alkan)
        self.second_window.show()
        self.close()