import os
from pathlib import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

DOCS_URL = "/docs"

# Load .ENV file variables
load_dotenv('.env', override=True)


class DefaultSettings(BaseSettings):
    # ENV STATE:
    ENV_STATE: str = 'default'
    # APP_CONFIG
    BASE_DIR: Path = Path(__file__).parent.parent
    SECRET_KEY: str = 'default'
    # # DATABASE CONFIG
    SQLALCHEMY_DATABASE_URL: str = "default"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SHOW_SQLALCHEMY_LOG_MESSAGES: bool = False
    # ALEMBIC CONFIG:
    ALEMBIC_TABLE_NAME: str = "alembic_version"
    # DOCS
    DOCS_URL: str | None = None

    class Config:
        env_file = ".env"


class LocalDevSettings(DefaultSettings):
    # ENV CONFIG
    ENV_STATE: str = "localdev"
    DEBUG_MODE: bool = True 
    # ORM CONFIG
    SQLALCHEMY_ECHO: bool = True
    # DOCS
    DOCS_URL: str | None = DOCS_URL


class DevSettings(DefaultSettings):
    # ENV CONFIG
    ENV_STATE: str = "dev"
    DEBUG_MODE: bool = True 
    # ORM CONFIG
    SQLALCHEMY_ECHO: bool = False
    # DOCS
    DOCS_URL: str | None = DOCS_URL


class TestQaSettings(DefaultSettings):
    # ENV CONFIG
    ENV_STATE: str = "testqa"
    DEBUG_MODE: bool = False 
    # ORM CONFIG
    SQLALCHEMY_ECHO: bool = False
    # DOCS
    DOCS_URL: str | None = DOCS_URL


class ProductionSettings(DefaultSettings):
    # ENV CONFIG
    ENV_STATE: str = "production"
    DEBUG_MODE: bool = False 
    # ORM CONFIG
    SQLALCHEMY_ECHO: bool = False
    # DOCS
    DOCS_URL: str | None = None



def get_settings() -> BaseSettings:
    env_state = os.getenv("ENV_STATE", "default")
    if env_state == "dev":
        return DevSettings()
    elif env_state == "testqa":
        return TestQaSettings()
    elif env_state == "production":
        return ProductionSettings()
    else:
        return LocalDevSettings()