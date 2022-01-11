from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from cryptography.exceptions import InvalidTag
from gui import *
from protect import *
import sys
import codecs

class SimpleTextLockbox(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.retranslateUi(window)
        self.openButton.clicked.connect(self.openFile)
        self.saveButton.clicked.connect(self.saveFile)
        self.encryptButton.clicked.connect(self.encryptFile)
        self.decryptButton.clicked.connect(self.decryptFile)
        self.exitButton.clicked.connect(self.exit)
        self.actionDescription.triggered.connect(self.description)
        self.actionIcon_Attributions.triggered.connect(self.attributions)
        self.actionHow_to_Use.triggered.connect(self.howToUse)

    def openFile(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Open File")
        if (len(fileName[0]) > 0):
            with codecs.open(fileName[0],'r', encoding='utf-8', errors='ignore') as f:
                self.textBox.setText(f.read())

    def saveFile(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(MainWindow, "Save File")
        if (len(fileName[0]) > 0):
            with open(fileName[0], 'w', errors='ignore') as f:
                plainText = self.textBox.toPlainText()
                f.write(plainText)

    def encryptFile(self):
        password, passwordEntered = QInputDialog.getText(self.centralwidget, "Password Dialog", "Enter a password: ", QLineEdit.Password)
        if passwordEntered:
            key = generateKey(password)
            plainText = self.textBox.toPlainText()
            cipherText = lock(key, plainText)
            self.textBox.setText(str(cipherText))

    def decryptFile(self):
        password, passwordEntered = QInputDialog.getText(self.centralwidget, "Password Dialog", "Enter a password: ", QLineEdit.Password)
        try:
            if passwordEntered:
                key = generateKey(password)
                cipherText = self.textBox.toPlainText()
                plainText = unlock(key, cipherText)
                self.textBox.setText(plainText)
        except (IndexError, NameError, SyntaxError, ValueError):
            popup.setText("Invalid file.")
            popup.exec_()
        except InvalidTag:
            popup.setText("The password that you have entered is incorrect.")
            popup.exec_()

    def exit(self):
        QCoreApplication.exit()

    def description(self):
        popup.setWindowTitle("Description")
        with open("resources/description.txt") as f:
            description = f.read()
        popup.setText(description)
        popup.exec_()

    def attributions(self):
        popup.setWindowTitle("Attributions")
        with open("resources/attributions.txt") as f:
            attributions = f.read()
        popup.setText(attributions)
        popup.exec_()

    def howToUse(self):
        popup.setWindowTitle("How to Use")
        with open("resources/howToUse.txt") as f:
            howToUse = f.read()
        popup.setText(howToUse)
        popup.exec_()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
retriever = QtWidgets.QMainWindow()
ui = SimpleTextLockbox(MainWindow)
popup = QMessageBox()

if __name__ == '__main__':
    MainWindow.show()
    app.exec_()
