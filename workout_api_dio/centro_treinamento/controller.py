from uuid import uuid4
from pydantic import UUID4
from fastapi import APIRouter, status, Body, HTTPException
from workout_api_dio.centro_treinamento.schemas import  CentroTreinamentoIn,CentroTreinamentoOut
from workout_api_dio.centro_treinamento.models import CentroTreinamentoModel

from workout_api_dio.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

router = APIRouter()
@router.post(
    '/',
    summary = 'Criar novo Ct',
    status_code = status.HTTP_201_CREATED,
    response_model = CentroTreinamentoOut,
)
async def post(
    db_session: DatabaseDependency,
    centro_treinamento_in: CentroTreinamentoIn = Body(...)
)-> CentroTreinamentoOut:
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(),**centro_treinamento_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())

    db_session.add(centro_treinamento_model)
    await db_session.commit()

    return centro_treinamento_out


@router.get(
    '/',
    summary = 'Consultar todas os CTs',
    status_code = status.HTTP_200_OK,
    response_model =list[CentroTreinamentoOut],
)
async def query(
    db_session: DatabaseDependency,
)-> list[CentroTreinamentoOut]:
    centro_treinamento_out: list[CentroTreinamentoOut] = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    return centro_treinamento_out

@router.get(
    '/{id}',
    summary = 'Consultar CT por ID',
    status_code = status.HTTP_200_OK,
    response_model =CentroTreinamentoOut,
)
async def query(id:UUID4,db_session: DatabaseDependency,)-> CentroTreinamentoOut:
    centro_treinamento_out: CentroTreinamentoOut = (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))).scalars().first()

    if not centro_treinamento_out:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'CT não encontrada para o id:{id}'
        )
    return centro_treinamento_out