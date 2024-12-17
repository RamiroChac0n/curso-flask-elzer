from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, ForeignKey
from datetime import datetime
from src.models.rol_model import Rol_model_db

class Usuario_model_db(db.Model):
    __tablename__ = 'usuario'

    # Campos
    id_usuario: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(200), nullable=False)
    correo: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(200), nullable=False)
    ultimo_acceso: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    id_rol = mapped_column(Integer, ForeignKey(Rol_model_db.id_rol), nullable=False)