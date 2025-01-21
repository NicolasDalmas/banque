from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_url = 'sqlite:///banque.db'

def get_engine():
    engine = create_engine(url= db_url)
    return engine

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind= engine)
    return Session()