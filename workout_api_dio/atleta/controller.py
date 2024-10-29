from uuid import uuid4
from datetime import datetime
from pydantic import UUID4
from fastapi import APIRouter, status, Body, HTTPException
from workout_api_dio.atleta.schemas import AtletaIn, AtletasOut,AtletaUpdate
from workout_api_dio.atleta.models import AtletaModel
from workout_api_dio.categorias.models import CategoriaModel
from workout_api_dio.centro_treinamento.models import CentroTreinamentoModel
from workout_api_dio.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

router = APIRouter()

@router.post(
    '/',
    summary='Criar novo atleta',
    status_code=status.HTTP_201_CREATED,
    response_model=AtletasOut,
)
async def post(
    db_session: DatabaseDependency,
    atleta_in: AtletaIn = Body(...)
):
    categoria_name = atleta_in.categoria.nome
    centrotreinamento_name = atleta_in.centro_treinamento.nome

    # Buscar categoria
    categoria = (await db_session.execute(
        select(CategoriaModel).filter_by(nome=categoria_name)
    )).scalars().first()

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Categoria {categoria_name} não encontrada'
        )

    # Buscar centro de treinamento
    centro_treinamento = (await db_session.execute(
        select(CentroTreinamentoModel).filter_by(nome=centrotreinamento_name)
    )).scalars().first()

    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Centro de treinamento: {centrotreinamento_name} não encontrado'
        )

    # Criar o atleta
    try:
        atleta_id = uuid4()
        atleta_out = AtletasOut(id=atleta_id, created_at=datetime.utcnow(), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={'categoria', 'centro_treinamento'}))
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id

        # Adicionar e confirmar o atleta
        db_session.add(atleta_model)
        await db_session.commit()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail='Erro ao salvar dados do atleta no banco'
        )
    return atleta_out

@router.get(
    '/',
    summary = 'Consultar todos os atletas',
    status_code = status.HTTP_200_OK,
    response_model =list[AtletasOut],
)
async def query(db_session: DatabaseDependency,)-> list[AtletasOut]:
    atletas: list[AtletasOut] = (await db_session.execute(select(AtletaModel))).scalars().all()

    return atletas


@router.get(
    '/{id}',
    summary = 'Consultar atleta por ID',
    status_code = status.HTTP_200_OK,
    response_model =AtletasOut,
)
async def query(id:UUID4,db_session: DatabaseDependency,)-> AtletasOut:
    atleta: AtletasOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Atleta não encontrada para o id:{id}'
        )
    return atleta

@router.patch(
    '/{id}',
    summary = 'Editar atleta por ID',
    status_code = status.HTTP_200_OK,
    response_model =AtletasOut,
)
async def query(id:UUID4,db_session: DatabaseDependency, atleta_up: AtletaUpdate =Body(...))-> AtletasOut:
    atleta: AtletasOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Atleta não encontrada para o id:{id}'
        )
    
    atleta_update = atleta_up.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta, key, value)

    await db_session.commit()
    await db_session.refresh(atleta)
    return atleta

@router.delete(
    '/{id}',
    summary = 'Deletar atleta por ID',
    status_code = status.HTTP_204_NO_CONTENT
)
async def get(id: UUID4, db_session: DatabaseDependency,)-> None:
    atleta: AtletasOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Atleta não encontrada para o id:{id}'
        )    
    
    await db_session.delete(atleta)
  
    await db_session.commit()
    