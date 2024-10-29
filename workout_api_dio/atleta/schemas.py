from pydantic import  Field, PositiveFloat
from typing import Annotated, Optional
from workout_api_dio.contrib.schemas import BaseSchema, OutMixin
from workout_api_dio.categorias.schemas import CategoriaIn
from workout_api_dio.centro_treinamento.schemas import CentroTreinamentoAtleta

class Atleta(BaseSchema):
    nome: Annotated[str,Field(description="Nome do atleta", example='Jefferson',max_length=50)]
    cpf: Annotated[str,Field(description="CPF do atleta", example='01234567890',max_length=11)]
    #idade: Annotated[int,Field(description="Idade do atleta", example=25,max_length=2)]
    idade: Annotated[int, Field(description="Idade do atleta", example=25, ge=0, le=99)]
    peso: Annotated[PositiveFloat,Field(description="Peso do atleta", example=60.2)]
    altura: Annotated[PositiveFloat,Field(description="Altura do atleta", example=1.8)]
    sexo: Annotated[str,Field(description="Genero do atleta", example='M',max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")]

class AtletaIn(Atleta):
    pass

class AtletasOut(Atleta,OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str],Field(None,description="Nome do atleta", example='Jefferson',max_length=50)]
    idade: Annotated[Optional[int], Field(None,description="Idade do atleta", example=25, ge=0, le=99)]