from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped,mapped_column

from app.base import Base

class Etapa(Base):
    __tablename__ = "etapas"

    id_etapa:Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        nullable = False
    )

    nombre:Mapped[str] = mapped_column(
        String(100),
        nullable = False,
        unique = True
    )

    descripcion:Mapped[str | None] = mapped_column(
        Text,
        nullable = True
    )

    orden:Mapped[int] = mapped_column(
        Integer,
        nullable = False,
        unique = True
    )