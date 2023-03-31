import add
from jogo import Jogo
from sqlalchemy import select

add.run()

print(add.session.query(Jogo).all())


stmt = select(Jogo)

for user in add.session.scalars(stmt):
    print(user)