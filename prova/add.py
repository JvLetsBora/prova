from sqlalchemy import create_engine
from base import Base
from jogo import Jogo
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///teste.db", echo=True)

Base.metadata.create_all(engine)


jogos = {
    "name":"DEAD SPACE REMAKE",
    "plataforma":"PS5", 
    "preco":350, 
    "quantidade": 10
    }

session = Session(engine)

def run():

    new_jogo = Jogo(quantidade=jogos["quantidade"],preco=jogos["preco"],plataforma=jogos["plataforma"],name=jogos["name"])
    session.add(new_jogo)
    session.commit()