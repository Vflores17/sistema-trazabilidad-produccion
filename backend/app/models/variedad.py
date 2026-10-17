from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.base import Base

class Variedad(Base):
    __tablename__ = "variedades"

    id_variedad:Mapped[int] = mapped_column(
        primary_key=True
    )

    nombre: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )

    descripcion: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

