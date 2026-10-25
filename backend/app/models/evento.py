from datetime import date
from sqlalchemy import Integer, String, Text,ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column

from app.base import Base

class Evento(Base):
    __tablename__ = "eventos"

    id_evento:Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        nullable = False
    )

    id_lote:Mapped[str] = mapped_column(
        String(50),
        ForeignKey("lotes.id_lote"),
        nullable = False
    )

    id_etapa:Mapped[int] = mapped_column(
        Integer,
        ForeignKey("etapas.id_etapa"),
        nullable = False
    )
    fecha:Mapped[date] = mapped_column(
        Date,
        nullable = False
    )

    tipo_evento:Mapped[str] = mapped_column(
        String(50),
        nullable = False
    )

    observacion:Mapped[str] = mapped_column(
        Text,
        nullable = False
    )

    accion_tratamiento:Mapped[str] = mapped_column(
        Text,
        nullable = True
    )
    estado:Mapped[str] = mapped_column(
        String(20),
        nullable = False
    )