import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from gui.bank import BankApp

app = QApplication(sys.argv) # Gestionnaire d'evenements Event Loop
MainWindow = QMainWindow()

gui = BankApp()
gui.setupUi(MainWindow)

MainWindow.show()
sys.exit(app.exec_())