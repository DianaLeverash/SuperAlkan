from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
import sqlite3

class History(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon(r'C:\Users\Diana\Desktop\Алканы PyQT\Проект Алканы\src\иконка.jpg'))

    def initUI(self):
        self.setWindowTitle('История поисковых запросов')
        uic.loadUi('История.ui', self)
        self.setFixedSize(self.size())
        self.history.setReadOnly(True)
        self.title.setReadOnly(True)
        self.work_BD()
        self.clean_history.clicked.connect(self.Clear_History)

    def work_BD(self):
        self.fileBD = sqlite3.connect("База данных.db")
        self.cursor = self.fileBD.cursor()
        self.cursor.execute("SElECT * FROM history")
        self.spisok = self.cursor.fetchall()
        self.fileBD.close()
        self.Set_history()

    def Set_history(self):
        print(self.spisok)
        from slovar import LoadFiles
        self.slovar = LoadFiles()
        result = ""
        for cort in self.spisok:
            infa = ""
            for el in self.slovar[cort[1]][0]:
                infa += el
            infa2 = ""
            for elem in self.slovar[cort[1]][1]:
                infa2 += elem
            result += str(cort[0]) + ". \t" + cort[1] + "\n" + infa + "\n" + infa2 + "\n"
        self.history.setText(result)
        if result == "":
            self.history.setText("Ваша история поисковых запросов пуста :)")

    def Clear_History(self):
        self.fileBD = sqlite3.connect("База данных.db")
        self.cursor = self.fileBD.cursor()
        self.cursor.execute("DELETE FROM history")
        self.fileBD.commit()
        self.fileBD.close()
        self.history.setText("Ваша история отчищена")