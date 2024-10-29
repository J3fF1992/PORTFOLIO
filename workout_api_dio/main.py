from fastapi import FastAPI 
from workout_api_dio.routers import api_router

app = FastAPI(title="Minha_Api_DIO")
if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app',host='0.0.0.0', port=8000, log_level='info',reload=True)

app.include_router(api_router)