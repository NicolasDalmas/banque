
from database.connexion import get_session
from database.models import Banque, Client


session = get_session()

def create_new_bank(nom):
    existing_bank = session.query(Banque).filter_by(nom= nom).first()

    if not existing_bank:
        bank = Banque(nom= nom)
        session.add(bank)
        session.commit()

def get_all_banks():
    banks = session.query(Banque).all()
    return [str(bank) for bank in banks]

def get_all_clients():
    clients = session.query(Client).all()
    return [str(client) for client in clients]

def get_last_recorded_bank():
    bank = session.query(Banque).order_by(Banque.id.desc()).first()
    return str(bank)

def get_last_recorded_client():
    client = session.query(Client).order_by(Client.id.desc()).first()
    return str(client)

def create_new_client(nom_banque, prenom, nom, ville, salaire):
    client = Client(nom, prenom, salaire, ville)
    bank = session.query(Banque).filter_by(nom= nom_banque).first()

    if bank:
        bank.ajouter_client(client)
        session.add(client)
        session.commit()

def generate_cb(nom_client):
    # destructuring data
    prenom, nom = nom_client.split(' ')
    client = session.query(Client).filter_by(nom= nom, prenom= prenom).first()

    if client:
        cb = client.banque.demande_carte_credit(client.compte)
        session.add(cb)
        session.commit()
        return cb