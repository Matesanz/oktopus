import json
import logging
import re
import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams
from sentence_transformers import SentenceTransformer

from oktopus.settings import config


def _chunk_text(document: str) -> list[str]:
    return [chunk.strip() for chunk in re.split(r"\n|\.", document)]


def _init_vectors_staff() -> tuple[SentenceTransformer, QdrantClient]:
    client = QdrantClient(path=config.QDRANT_LOCAL_PATH)  # Persist changes to disk
    client.recreate_collection(
        collection_name=config.QDRANT_COLL_NAME,
        vectors_config=VectorParams(size=config.MODEL_EMB_DIM, distance=Distance.COSINE),
    )
    model = SentenceTransformer(config.MODEL_NAME)
    assert model.get_sentence_embedding_dimension() == config.MODEL_EMB_DIM, f"{model.get_sentence_embedding_dimension() = } VS {MODEL_EMB_DIM = }"
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
    model, client = _init_vectors_staff()

    num_docs = len(list(config.PATH_DATA.glob('*.md')))
    points = [(0.0, 0.0)]
    for doc_idx, md_doc in enumerate(config.PATH_DATA.glob("*.md")):
        document_content = md_doc.read_text()
        _upload_one_document(model, client, document_content, doc_idx, points[doc_idx], md_doc.name.removesuffix('.md'))
    logging.warning(f"There are {num_docs} documents successfully loaded in qdrant 🥳🥳🥳🥳")


if __name__ == "__main__":
    _populate_db_qdrant()
