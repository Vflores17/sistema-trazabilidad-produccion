from datetime import date
from sqlalchemy import String,Date,ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column

from app.base import Base

class tandaSiembra (Base):
    __tablename__ = "tandas_siembra"

    id_tanda:Mapped[int] = mapped_column(
        primary_key = True
    )

    id_lote:Mapped[str] = mapped_column(
        String(50),
        ForeignKey("lotes.id_lote"),
        nullable = False
    )

    fecha_siembra:Mapped[date] = mapped_column(
        Date,
        nullable = False
    )

    observacion:Mapped[str | None] = mapped_column(
        String(200),
        nullable = True
    )

    
