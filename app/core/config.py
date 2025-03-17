from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    POSTGRES_DB: str
    PATH_DB: str
    AI_TOKEN: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    class Config:
        env_file = ".env"


settings = Settings()