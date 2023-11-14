import sqlite3
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QMovie
from Третье_окно import Izomers
from Четвертое_окно import History


class Beginning(QMainWindow):
    def __init__(self, Class2):
        self.Class2 = Class2
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Добро пожаловать! ;)")
        uic.loadUi("Проект по Яндексу(Алканы и изомеры) 1.ui", self)
        self.setFixedSize(self.size())
        self.gif = QMovie("eten.gif")
        self.gifka.setMovie(self.gif)
        self.gif.start()
        self.ButtonBeginning.clicked.connect(self.Naznachenie_Kluchevogo_slova)
        self.watching_history.clicked.connect(self.History)
        self.textEdit_2.setReadOnly(True)
        self.textEdit.setReadOnly(True)

    def Naznachenie_Kluchevogo_slova(self):
        self.alkan = self.VvodAlkana.text()
        from slovar import LoadFiles
        self.slovar = LoadFiles()
        if self.slovar.get(self.alkan) != None:
            self.Insertion_BD()
            self.second_window = self.Class2(Beginning, Izomers, self.alkan)
            self.second_window.show()
            self.close()
        else:
            self.VvodAlkana.setText("Ошибка, попробуйте снова! ;)")

    def Insertion_BD(self):
        self.fileBD = sqlite3.connect("База данных.db")
        self.cursor = self.fileBD.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY,
        alkan TEXT NOT NULL)''')
        self.cursor.execute("INSERT INTO history (alkan) VALUES (?)", [self.alkan])
        self.fileBD.commit()
        self.fileBD.close()

    def History(self):
        self.second_window = History()
        self.second_window.show()