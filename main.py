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
        popup.setText("""This program allows the user to encrypt the contents of any file and then decrypt those contents. A unique key is generated from a password entered by the user. Hence this program effectively allows the user to password protect the text within files.\n
AES (Advanced Encryption Standard) is implemented using the Python cryptography module.\n
AES: https://en.wikipedia.org/wiki/Advanced_Encryption_Standard\n
Python Cryptography Module: https://pypi.org/project/cryptography/\n""")
        popup.exec_()

    def attributions(self):
        popup.setWindowTitle("Attributions")
        popup.setText("Icons made by Freepik from https://www.flaticon.com/\nIcon Author: https://www.flaticon.com/authors/freepik")
        popup.exec_()

    def howToUse(self):
        popup.setWindowTitle("How to Use")
        popup.setText("""First either enter your own text into the text box on the right or click on the \"Open\" button. The \"Open\" button will open up your file explorer. Search for the file that you would like to encrypt and click on it. The contents of the file will then be put into the text box.\nThen click on the \"Encrypt Contents\" button. You will be prompted to enter a password. After entering a password, the contents will be encrypted. You can then click on the \"Save Contents\" button to save your file.\nTo decrypt a file, make sure that you have opened a file whose contents have already been encrypted. Then click on \"Decrypt Contents\" button. You will be prompted to enter the password which you have used to encrypt the contents of this file. Enter this password again and the encrypted contents will become decrypted and displayed in the text box.\n""")
        popup.exec_()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
retriever = QtWidgets.QMainWindow()
ui = SimpleTextLockbox(MainWindow)
popup = QMessageBox()

if __name__ == '__main__':
    MainWindow.show()
    app.exec_()
