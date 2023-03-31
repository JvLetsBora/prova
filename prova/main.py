import add
from jogo import Jogo


add.run()

print(add.session.query(Jogo).all())


