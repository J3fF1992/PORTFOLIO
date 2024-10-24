from fastapi import APIRouter
from workout_api_dio.atleta.controller import router as atleta

api_router = APIRouter()
api_router.include_router(atleta, prefix="/atleta", tags=["Atleta"])