from datetime import date
from sqlalchemy import String, Integer, Date, CheckConstraint, ForeignKey,Text
from sqlalchemy.orm import Mapped, mapped_column

from app.base import Base

class Movimiento(Base):
    __tablename__= "movimientos"

    id_movimiento:Mapped[int] = mapped_column(
        primary_key = True,
        nullable = False
    )

    id_lote:Mapped[str] = mapped_column(
        String(50),
        ForeignKey("lotes.id_lote"),
        nullable = False
    )

    id_etapa_origen:Mapped[int] = mapped_column(
        Integer,
        ForeignKey("etapas.id_etapa"),
        nullable = False
    )

    id_etapa_destino:Mapped[int] = mapped_column(
            Integer,
            ForeignKey("etapas.id_etapa"),
            nullable = False
    )

    fecha:Mapped[date] = mapped_column(
        Date, 
        nullable=False
    ) 

    cantidad_bandejas:Mapped[int] = mapped_column(
        Integer,
        nullable = False
    )

    observacion:Mapped[str | None]= mapped_column(
        Text,
        nullable = True
    )

    __table_args__ = (
        CheckConstraint(
            "cantidad_bandejas > 0",
            name = "ck_cantidad_bandejas_positiva"
        ),
    )
