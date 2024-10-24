from pydantic import  Field, PositiveFloat
from typing import Annotated
from workout_api_dio.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str,Field(description="Nome do atleta", example='Jefferson',max_length=50)]
    cpf: Annotated[int,Field(description="CPF do atleta", example='01234567890',max_length=11)]
    idade: Annotated[int,Field(description="Idade do atleta", example=25,max_length=2)]
    peso: Annotated[PositiveFloat,Field(description="Peso do atleta", example=60.2)]
    altura: Annotated[PositiveFloat,Field(description="Altura do atleta", example=1.8)]
    sexo: Annotated[str,Field(description="Genero do atleta", example='M',max_length=1)]

class AtletaIn(Atleta):
    pass

class AtletasOut(Atleta,OutMixin):
    pass