"""
On veut simuler le fonctionnement de banques
Une banque a un nom et une liste de clients
Un client a un nom prenom salaire ville comme attributs
Une banque peut ajouter un client a sa liste ce qui va creer son compte
Un compte a un numero de 7 chiffres generes aleatoirement (10000000 et 9999999) et un solde, on peut retirer et deposer de l'argent sur le compte
Une banque peut faire une demande de carte de credit pour le compte d'un client
Une carte de credit a un numero de 16 chiffres generes aleatoirement de type (XXXX XXXX XXXX XXXX), un cvv de 3 chiffres generes aleatoirement de type (XXX) et une date d'expiration 5 ans apres la date de creation (MM/YY)
"""
# Le __init__ doit etre vide de toute logique metier
# Le principe de separation des preoccupations

# 1/ tu detectes les classes
# 2/ ecrire les __init__
# 3/ Ecrire les __repr__



from database.connexion import get_session
from database.models import Banque, Client

session = get_session()

bnp = Banque(nom= "BNP Paribas")
session.add(bnp)

alice = Client(nom= "Bowman", prenom= "Alice", salaire= 3000, ville= "Paris")
john = Client(nom= "Doe", prenom= "John", salaire= 3000, ville= "Lille", depot_initial = 300)
print(alice.compte)
print(john.compte)
session.add(alice)
session.add(john)

bnp.ajouter_client(alice)
bnp.ajouter_client(john)

cb_alice = bnp.demande_carte_credit(alice.compte)
print(cb_alice)
session.add(cb_alice)

session.commit()