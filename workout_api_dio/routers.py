from fastapi import APIRouter
from workout_api_dio.atleta.controller import router as atleta
from workout_api_dio.categorias.controller import router as categorias
from workout_api_dio.centro_treinamento.controller import router as centro_treinamento

api_router = APIRouter()
api_router.include_router(atleta, prefix="/atletas", tags=["ATLETA"])
api_router.include_router(categorias, prefix="/categorias", tags=["CATEGORIA"])
api_router.include_router(centro_treinamento, prefix="/centro_treinamento", tags=["CT"])