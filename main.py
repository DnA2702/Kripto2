import sys
from tkinter import Widget
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

from streamcipher import *

import sqlite3
import os
import csv
import datetime
import random

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("main.ui", self)
        self.pushButton_6.clicked.connect(self.Encrypt)
        self.pushButton_7.clicked.connect(self.Decrypt)
        self.pushButton_11.clicked.connect(self.AddFile)
        self.pushButton_8.clicked.connect(self.Default)
        self.pushButton_8.clicked.connect(self.Base64)
        self.pushButton_12.clicked.connect(self.Save)

    def Encrypt(self):
        plaintext = self.textEdit.toPlainText()
        key_awal = self.textEdit_2.toPlainText()
        key_tmp = [x for x in key_awal]
        result = prga(ksa(keyMakers(key_tmp)), plaintext)
        self.textBrowser.setText(result)

        # keyFinal = create_kunci(plaintext_tmp, key_tmp)
        # result = extended_vigenere_encrypt(plaintext_tmp, keyFinal)
        # self.textBrowser.setText(result)

    def Decrypt(self):
        ciphertext_awal = self.textEdit.toPlainText()
        ciphertext_tmp = [x for x in ciphertext_awal]
        key_awal = self.textEdit_2.toPlainText()
        key_tmp = [x for x in key_awal]
        
        # keyFinal = create_kunci(ciphertext_tmp, key_tmp)
        # result = extended_vigenere_decrypt(ciphertext_tmp, keyFinal)
        # self.textBrowser.setText(result)
    
    def AddFile(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File", "E:\Kripto\kriptomanjaa", "All Files (*)")
        text = ""
        with open(fname[0], "rb") as f:
            while True:
                b = f.read(1)
                if not b:
                    break
                text += chr(int.from_bytes(b, byteorder="big"))
        self.textEdit.setPlainText(str(text))

    def Default(self):
        output = []
        text_awal = self.textBrowser.toPlainText()
        text_tmp = [x for x in text_awal]
        for i in range(len(text_tmp)):
            if (text_tmp[i] != ' '):
                output.append(text_tmp[i])
        self.textBrowser.setText(''.join(output))

    def Base64(self):
        print()

    def Save(self):
        name = QFileDialog.getSaveFileName(self, "Save File")
        file = open(name[0], 'w')
        text = self.textBrowser.toPlainText()
        file.write(text)
        file.close()

# main
app = QApplication(sys.argv)
welcome = Menu()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exit Program")