from pydantic import  Field,UUID4
from typing import Annotated
from workout_api_dio.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str,Field(description="Nome do centro de treinamento", example='Ct Dos Titãns',max_length=20)]
    endereco: Annotated[str,Field(description="Endereco", example='Rua Jão da silva',max_length=60)]
    proprietario: Annotated[str,Field(description="Nome do proprietario", example='Maria Dos Titãns',max_length=30)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str,Field(description="Nome do centro de treinamento", example='Ct Dos Titãns',max_length=20)]


class CentroTreinamentoOut(CentroTreinamentoIn):
     id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]