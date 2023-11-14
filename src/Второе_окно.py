from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class Alkanes(QMainWindow):
    def __init__(self, Class1, Class3, alkan):
        self.Class1 = Class1
        self.Class3 = Class3
        self.alkan = alkan
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Алканы")
        self.slovar = {}
        uic.loadUi("Проект по Яндексу(Алканы и изомеры) 2.ui", self)
        self.setFixedSize(self.size())
        self.LoadFile()
        self.LoadAlkan(self.alkan)
        self.izomerButton.clicked.connect(self.GoTo3)
        self.returnOnFirst.clicked.connect(self.Return1)
        self.nameAlkan.setReadOnly(True)
        self.infaAlkan.setReadOnly(True)

    def LoadFile(self):
        from slovar import LoadFiles
        self.slovar = LoadFiles()

    def LoadAlkan(self, alkan_name):
        self.nameAlkan.setText(alkan_name)
        stroka = ""
        for elem in self.slovar[alkan_name.lower()][0]:
            stroka += elem
        self.infaAlkan.setText(stroka)

    def Return1(self):
        self.first_window = self.Class1(Alkanes)
        self.first_window.show()
        self.close()

    def GoTo3(self):
        self.third_window = self.Class3(self.Class1, Alkanes, self.alkan)
        self.third_window.show()
        self.close()