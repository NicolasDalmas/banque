from random import randint
from datetime import datetime, timedelta
from typing import List

from sqlalchemy import DECIMAL, Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

from database.connexion import get_engine

Base = declarative_base() # va creer une classe
engine = get_engine()

class Compte(Base):
    __tablename__ = 'compte'

    id = Column(Integer, primary_key= True, autoincrement= True)
    numero = Column(Integer, nullable= False)
    solde = Column(DECIMAL, nullable= False, default= 0.0)

    # cles etrangeres
    client_id = Column(Integer, ForeignKey('client.id'), nullable= False)
    carte_credit_id = Column(Integer, ForeignKey('carte_credit.id'))

    # Relations
    client = relationship('Client', back_populates= 'compte')
    carte_credit = relationship('CarteCredit', back_populates= 'compte')

    def __init__(self, solde: float = 0) -> None:
        self.numero = randint(1000000, 9999999)
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant > self.solde:
            raise Exception("Fonds insuffisants")
        self.solde -= montant

    def __repr__(self) -> str:
        return f"Compte({self.numero} - solde= {self.solde})"

class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key= True, autoincrement= True)
    nom = Column(String, nullable= False)
    prenom = Column(String, nullable= False)
    salaire = Column(String)
    ville = Column(String)

    # Cles etrangeres
    banque_id = Column(Integer, ForeignKey('banque.id'), nullable= False)

    # Relations
    banque = relationship('Banque', back_populates= 'clients')
    compte = relationship('Compte', back_populates= 'client', uselist= False)


    def __init__(self,nom: str, prenom: str, salaire: float, ville: str, depot_initial: float = 0):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.ville = ville
        self.compte = Compte(depot_initial)

    def __repr__(self) -> str:
        return f"{self.prenom} {self.nom}"

class Banque(Base):
    __tablename__ = 'banque'

    id = Column(Integer, primary_key= True, autoincrement= True)
    nom = Column(String, nullable= False)

    # Relations
    clients = relationship('Client', back_populates= 'banque', uselist= True) #type: ignore



    def __init__(self, nom: str):
        self.nom = nom
        self.clients: List[Client] = []

    def ajouter_client(self, client: Client):
        self.clients.append(client)

    def demande_carte_credit(self, compte: Compte):
        cb = CarteCredit(compte)
        return cb

    def __repr__(self) -> str:
        return f"{self.nom}"

class CarteCredit(Base):
    __tablename__ = 'carte_credit'

    id = Column(Integer, primary_key= True, autoincrement= True)
    numero = Column(String, nullable= False)
    cvv = Column(String, nullable= False)
    date_expiration = Column(String, nullable= False)

    # Relations
    compte = relationship('Compte', back_populates= 'carte_credit', uselist= False)


    def __init__(self, compte: Compte) -> None:
        self.numero = self.generer_numero_carte()
        self.cvv = self.generer_cvv()
        self.date_expiration = self.generer_date_expiration()
        self.compte = compte

    def generer_numero_carte(self):
        card_number = ''.join([str(randint(0, 9)) for i in range(16)])
        return ' '.join([card_number[i: i + 4] for i in range(0, 16, 4)])
    
    def generer_cvv(self):
        return ''.join([str(randint(0,9)) for i in range(3)])
    
    def generer_date_expiration(self):
        auj = datetime.now()
        date_5_ans = auj + timedelta(days= 365 * 5)
        return date_5_ans.strftime('%m/%y')
    
    def __repr__(self) -> str:
        return f"{self.numero} - {self.date_expiration} - {self.cvv}"

Base.metadata.create_all(engine)