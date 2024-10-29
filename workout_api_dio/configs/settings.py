from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://user:123456@localhost/mydb')

settings= Settings()

#teste funcional