"""
This module contains the general settings of the Oktopus project.

Settings can be set via environment variables or a .env file.
"""
from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    """Oktopus general settings.

    Settings can be set via environment variables or a .env file.

    Attributes:
        PATH_DATA (Path): Path to the folder containing the files.
        QDRANT_LOCAL_PATH (Path): Path to the Qdrant Database.
        QDRANT_COLL_NAME (str): Name of the Qdrant collection.
        MODEL_NAME (str): Name of the sentence-transformers model.
        MODEL_EMB_DIM (int): Embedding length of the sentence-transformers model.
    """

    PATH_DATA: Path = Path(__file__).parent.parent / "data"
    QDRANT_LOCAL_PATH: Path = Path(__file__).parent.parent / "data"
    QDRANT_COLL_NAME: str = "oktopus"
    MODEL_NAME: str = "sentence-transformers/multi-qa-MiniLM-L6-cos-v1"
    MODEL_EMB_DIM: int = 384

config = Settings()
