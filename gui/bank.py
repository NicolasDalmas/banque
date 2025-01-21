

from PyQt5.QtWidgets import QMessageBox

from gui.app import Ui_MainWindow
from gui.gui_initialization import GuiInitialization
from gui.signal_management import SignalManagement
from logic import actions

# POO: Casser le couplage fort
# Separation des preoccupations

class BankApp(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.gui_init = GuiInitialization(self ,actions)
        self.signal_mngt = SignalManagement(self)
        self.init_gui()

    def init_gui(self):
        self.gui_init.connect_buttons()
        self.gui_init.fill_lists()
        self.signal_mngt.connect_signals()

    def create_bank(self):
        bank_name = self.bank_name_input.text()
        actions.create_new_bank(nom= bank_name)
        self.signal_mngt.created_bank_signal.emit()
        QMessageBox.information(None, 'Nouvelle banque', f"La banque '{bank_name}' a bien ete cree ")
        self.bank_name_input.clear()

    def create_client(self):
        prenom = self.prenom_client_input.text()
        nom = self.nom_client_input.text()
        ville = self.ville_client_input.text()
        salaire = self.salaire_client_input.text()
        nom_banque = self.list_banques.currentText()

        actions.create_new_client(nom_banque, prenom, nom, ville, salaire)
        self.signal_mngt.created_client_signal.emit()
        QMessageBox.information(None, 'Nouveau client', f"Le client {prenom} {nom} a bien ete cree ")

        self.prenom_client_input.clear()
        self.nom_client_input.clear()
        self.ville_client_input.clear()
        self.salaire_client_input.clear()

    def update_list_banques(self):
        self.list_banques.addItem(actions.get_last_recorded_bank())

    def update_list_clients(self):
        self.list_clients.addItem(actions.get_last_recorded_client())

    def generate_cb(self):
        nom_client = self.list_clients.currentText()
        cb = actions.generate_cb(nom_client)
        QMessageBox.information(None, 'Nouvelle CB', f"La CB: '{cb}' a bien ete cree ")

# SOLID
# Single Responsibility
# Open/Closed Principle : Une classe doit etre fermer a la modification et ouverte a l'extension