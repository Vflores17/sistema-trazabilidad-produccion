from sqlalchemy import String,Integer,CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped

from app.base import Base

class detalleBandeja(Base):
    __tablename__ = "detalles_bandeja"

    id_detalle:Mapped[int] = mapped_column(
        primary_key = True,
        nullable = False
    )

    id_tanda:Mapped[int] = mapped_column(
        ForeignKey("tandas_siembra.id_tanda"),
        nullable = False
    )

    numero_en_tanda:Mapped[int] = mapped_column(
        Integer,
        nullable = False
    )

    cantidad_semillas:Mapped[int] = mapped_column(
        Integer,
        nullable = False
    )

    observacion:Mapped[str | None] = mapped_column(
        Text,
        nullable = True
    )

    __table_args__ = (
    CheckConstraint(
        "numero_en_tanda > 0",
        name="ck_detalles_bandeja_numero_positivo"
    ),
    CheckConstraint(
        "cantidad_semillas > 0",
        name="ck_detalles_bandeja_semillas_positivas"
    )
)