from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gui.bank import BankApp


class GuiInitialization:

    def __init__(self, app: 'BankApp', actions):
        self.app = app
        self.actions = actions

    def connect_buttons(self):
        self.app.create_bank_btn.clicked.connect(self.app.create_bank)
        self.app.create_client_btn.clicked.connect(self.app.create_client)
        self.app.generate_cb_btn.clicked.connect(self.app.generate_cb)

    def fill_lists(self):
        self.app.list_banques.addItems(self.actions.get_all_banks())
        self.app.list_clients.addItems(self.actions.get_all_clients())