from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

class Rol_model_db(db.Model):
    __tablename__ = 'rol'

    id_rol: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)    