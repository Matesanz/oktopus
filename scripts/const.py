from pathlib import Path

PATH_DATA = Path(__file__).parent.parent / "data"
QDRANT_LOCAL_PATH = Path(__file__).parent.parent / "data"
QDRANT_COLL_NAME = "oktopus"
MODEL_NAME = "sentence-transformers/multi-qa-MiniLM-L6-cos-v1"
MODEL_EMB_DIM = 384
