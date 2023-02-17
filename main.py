import sys
from tkinter import Widget
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

from streamcipher import *
from extended_vigenere import *

import sqlite3
import os
import csv
import datetime
import random

class Menu(QMainWindow):
    
    temp = ''
    state = True
    
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
        K = keyMakers(key_tmp)
        plaintext = [x for x in plaintext]
        P = extended_vigenere_encrypt(plaintext, create_kunci(plaintext, key_tmp))
        result = prga(ksa(K), P)
        self.textBrowser.setText(result)
        Menu.state = True

    def Decrypt(self):
        ciphertext = self.textEdit.toPlainText()
        ciphertext = [x for x in ciphertext]
        key_awal = self.textEdit_2.toPlainText()
        key_tmp = [x for x in key_awal]
        K = keyMakers(key_tmp)
        temp = prga(ksa(K), ciphertext)
        result = extended_vigenere_decrypt(temp, create_kunci(temp, key_tmp))
        self.textBrowser.setText(result)
        Menu.state = False
    
    def AddFile(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File")
        bin_data = open(fname[0], "rb").read()
        string = bin_data.decode("latin1")
        Menu.temp = string
        self.textEdit.setPlainText(string)

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
        if (Menu.temp == ""):
            name = QFileDialog.getSaveFileName(self, "Save File")
            with open(name[0], "wb") as file:
                file.write(self.textBrowser.toPlainText().encode("latin1"))
        else:
            if (Menu.state):
                name = QFileDialog.getSaveFileName(self, "Save File")
                key_awal = self.textEdit_2.toPlainText()
                key_tmp = [x for x in key_awal]
                K = keyMakers(key_tmp)
                plaintext = [x for x in Menu.temp]
                P = extended_vigenere_encrypt(plaintext, create_kunci(plaintext, key_tmp))
                result = prga(ksa(K), P)
                with open(name[0], "wb") as file:
                    file.write(result.encode("latin1"))
            else:
                name = QFileDialog.getSaveFileName(self, "Save File")
                ciphertext = [x for x in Menu.temp]
                key_awal = self.textEdit_2.toPlainText()
                key_tmp = [x for x in key_awal]
                K = keyMakers(key_tmp)
                temp = prga(ksa(K), ciphertext)
                result = extended_vigenere_decrypt(temp, create_kunci(temp, key_tmp))
                with open(name[0], "wb") as file:
                    file.write(result.encode("latin1"))
        Menu.temp = ""

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