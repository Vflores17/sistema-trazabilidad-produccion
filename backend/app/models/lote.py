from datetime import date
from sqlalchemy import String, Text, CheckConstraint, Date, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.base import Base

class Lote(Base):
    __tablename__ = "lotes"

    id_lote: Mapped[str] = mapped_column(
        String(50),
        primary_key = True
    )

    id_proveedor: Mapped[int] = mapped_column(
        ForeignKey("proveedores.id_proveedor"),
        nullable=False
    )

    id_variedad: Mapped[int] = mapped_column(
        ForeignKey("variedades.id_variedad"),
        nullable=False
    )

    fecha_inicio:Mapped[date]=mapped_column(
        Date,
        nullable=False
    )
    cantidad_estimada:Mapped[int]=mapped_column(
        Integer,
        nullable=False
    )
    observacion:Mapped[str | None]=mapped_column(
        Text,
        nullable=True
    )

    __table_args__ = (
        CheckConstraint(
            "cantidad_estimada > 0",
            name="ck_lotes_cantidad_estimada_positiva"
        ),
    )  
