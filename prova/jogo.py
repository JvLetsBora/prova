from base import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Jogo(Base):
    __tablename__ = "jogo"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    plataforma: Mapped[str] = mapped_column(String(30))
    preco: Mapped[int] = mapped_column(Integer)
    quantidade: Mapped[int] = mapped_column(Integer)
