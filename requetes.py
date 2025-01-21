from database.connexion import get_session
from database.models import Client


session = get_session()

clients = session.query(Client).all()
print(clients)

alice = session.query(Client).filter_by(prenom= 'Alice').one()
print(alice)
print(alice.banque)
print(alice.compte)
print(alice.compte.carte_credit)