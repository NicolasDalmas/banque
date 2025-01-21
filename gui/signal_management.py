from PyQt5.QtCore import QObject, pyqtSignal

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gui.bank import BankApp

class SignalManagement(QObject):
    created_bank_signal = pyqtSignal()
    created_client_signal = pyqtSignal()

    def __init__(self, app : 'BankApp'):
        super().__init__()
        self.app = app

    def connect_signals(self):
        self.created_bank_signal.connect(self.app.update_list_banques)
        self.created_client_signal.connect(self.app.update_list_clients)