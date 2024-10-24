from workout_api_dio.contrib.schemas import BaseSchema
from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat

class Categoria(BaseSchema):
    nome:Annotated[str,Field(description="Nome da categoria", example='Scale',max_length=10)]
