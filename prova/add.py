from sqlalchemy import create_engine
from base import Base
from jogo import Jogo
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///teste.db", echo=True)

Base.metadata.create_all(engine)


jogos = [
    {
    "name":"DEAD SPACE REMAKE",
    "plataforma":"PS5", 
    "preco":350, 
    "quantidade": 10
    },
    {
    "name":"FORSPOKEN",
    "plataforma":"PC", 
    "preco":299, 
    "quantidade": 8
    },
    {
    "name":"DEAD ISLAND 2",
    "plataforma":"PS5", 
    "preco":350, 
    "quantidade": 10
    },
        {
    "name":"HOGWARTS LEGACY",
    "plataforma":"PC", 
    "preco":219, 
    "quantidade": 7
    },
    {
    "name":"WILD HEARTS",
    "plataforma":"XBox Series", 
    "preco":350, 
    "quantidade": 7
    },
    {
    "name":"RESIDENT EVIL 4",
    "plataforma":"PS5", 
    "preco":289, 
    "quantidade": 10
    },
    {
    "name":"THE LEGEND OF ZELDA: TEARS OF THE KINGDOM",
    "plataforma":"Switch", 
    "preco":350, 
    "quantidade": 10
    }
]

session = Session(engine)

def run():
    for add in jogos:
        print(add["name"])
        new_jogo = Jogo(quantidade=add["quantidade"],preco=add["preco"],plataforma=add["plataforma"],name=add["name"])
        session.add(new_jogo)
    session.commit()