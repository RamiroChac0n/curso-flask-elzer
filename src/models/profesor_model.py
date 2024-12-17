from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, ForeignKey
from datetime import datetime
from src.models.usuario_model import Usuario_model_db

class Profesor_model_db(db.Model):
    __tablename__ = 'profesor'

    # Campos
    id_profesor: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(200), nullable=False)
    apellido: Mapped[str] = mapped_column(String(200), nullable=False)
    registro: Mapped[int] = mapped_column(Integer, nullable=False)
    id_usuario= mapped_column(Integer, ForeignKey(Usuario_model_db.id_usuario), nullable=False)