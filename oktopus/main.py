"""Main Oktopus app.

To run it locally:

```
uvicorn oktopus.main:app --reload
```

Then go to http://localhost:8000/docs to see the API documentation.
"""
import logging
from time import monotonic

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

from oktopus.data_models import DocNode, Document, Query, DocumentScore
from oktopus.chunk2vector import populate_db_qdrant
from oktopus.settings import config
import json

docs_metadata: dict = json.loads(config.PATH_META_DATA.read_text())
id2metadata = {v['index']:DocNode(id=v['index'], x=v['x'], y=v['y'], title=k.removesuffix('.md')) for k, v in docs_metadata.items()}
model = SentenceTransformer(config.MODEL_NAME)


def _qdrant_payload_to_score(qdrant_response) -> DocumentScore:
    id = qdrant_response.payload['doc_id']
    x = qdrant_response.payload['doc_id']
    y = qdrant_response.payload['doc_id']
    title = qdrant_response.payload['title']
    chunk = qdrant_response.payload['chunk']
    score = qdrant_response.score

    return DocumentScore(id=id, x=x, y=y, title=title, score=score, chunk=chunk)


def search_in_qdrant(text: str, limit: int) -> list[DocumentScore]:
    tic = monotonic()
    client = QdrantClient(path=config.QDRANT_LOCAL_PATH)
    response_search = client.search(
        collection_name=config.QDRANT_COLL_NAME,
        query_vector=model.encode(text),
        limit=limit,
    )
    logging.warning(f"query took {monotonic() - tic:.2f}")
    return [_qdrant_payload_to_score(qdrant_response) for qdrant_response in response_search]



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    populate_db_qdrant()
    yield

app = FastAPI(lifespan=lifespan)

# cors
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


# Endpoints
@app.get("/documents", response_model=list[DocNode])
async def get_documents() -> list[DocNode]:
    """Get all documents from the database.

    Returns:
        List[DocNode]: List of documents
    """
    return list(id2metadata.values())


@app.post("/search", response_model=list[DocumentScore])
async def search(query: str) -> list[DocumentScore]:
    """Given a question (query) retrieves the scores for all the documents.

    Scores relates to the cosine similarity between the query and the document.

    Args:
        query (Query): Question to be answered by Oktopus based on your data.

    Returns:
        List[Tuple[int, float]]: List of (doc_id, score) tuples
    """
    def _filter_unique_document(documents: list[DocumentScore]) -> list[DocumentScore]:
        unique_id = set()
        unique_docs = []
        for doc in documents:
            if doc.id not in unique_id:
                unique_id.add(doc.id)
                unique_docs.append(doc)
        return unique_docs

    # Simulated score generation, returning doc_id and a score
    documents_found = search_in_qdrant(query, 5)

    return _filter_unique_document(documents_found)


@app.get("/documents/{doc_id}")
async def get_document_by_id(doc_id: int) -> str:
    """Retrieve a document by its id.

    Args:
        doc_id (int): Document id

    Returns:
        Document: Document
    """
    doc = id2metadata[doc_id].title + ".md"
    return (config.PATH_DOCS / doc).read_text()


# frontend
# app.mount("/", app=StaticFiles(directory="/static", html=True), name="static")