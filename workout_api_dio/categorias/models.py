from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from workout_api_dio.contrib.models import BaseModel

class CategoriaModel(BaseModel):
    __tablename__ = 'categoria'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    atletas: Mapped['AtletaModel'] = relationship("AtletaModel", back_populates="categoria")
