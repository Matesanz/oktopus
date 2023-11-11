import json
import logging
import re
import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams
from sentence_transformers import SentenceTransformer

from oktopus.settings import config


def _chunk_text(document: str) -> list[str]:
    return [chunk.strip() for chunk in document.split(".")]


def _init_vectors_staff() -> tuple[SentenceTransformer, QdrantClient]:
    client = QdrantClient(path=config.QDRANT_LOCAL_PATH)  # Persist changes to disk
    client.recreate_collection(
        collection_name=config.QDRANT_COLL_NAME,
        vectors_config=VectorParams(size=config.MODEL_EMB_DIM, distance=Distance.COSINE),
    )
    model = SentenceTransformer(config.MODEL_NAME)
    assert model.get_sentence_embedding_dimension() == config.MODEL_EMB_DIM, f"{model.get_sentence_embedding_dimension() = } VS {config.MODEL_EMB_DIM = }"
    return model, client


def _upload_one_document(
    model: SentenceTransformer, client: QdrantClient, document: str, doc_id: int, point: tuple[float, float], title: str
):
    chunks = _chunk_text(document)
    client.upsert(
        collection_name=config.QDRANT_COLL_NAME,
        points=[
            PointStruct(
                id=str(uuid.uuid4()),
                vector=model.encode(chunk).tolist(),
                payload={
                    "doc_id": doc_id,
                    "chunk": chunk,
                    "x": point[0],
                    "y": point[1],
                    "title": title
                },
            )
            for chunk in chunks
        ],
    )


def _populate_db_qdrant():
    logging.warning(f"👷👷 Starting to populate qdrant database ....")
    model, client = _init_vectors_staff()

    path_metadata = config.PATH_DATA / "documents-meta.json"
    assert path_metadata.exists()

    meta_data = json.loads(path_metadata.read_text())
    for md_doc in config.PATH_DOCS.glob("*.md"):
        file_name = md_doc.name
        document_content = md_doc.read_text()
        _upload_one_document(model,
                             client,
                             document_content,
                             meta_data[file_name]['index'],
                             (meta_data[file_name]["x"], meta_data[file_name]["y"]),
                             file_name.removesuffix('.md')
        )
    logging.warning(f"There are {len(meta_data)} documents successfully loaded in qdrant 🥳🥳🥳🥳")
    client.close()


if __name__ == "__main__":
    _populate_db_qdrant()
