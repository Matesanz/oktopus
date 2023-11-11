"""Main Oktopus app.

To run it locally:

```
uvicorn oktopus.main:app --reload
```

Then go to http://localhost:8000/docs to see the API documentation.
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from oktopus.data_models import DocNode, Document, Query
from oktopus import db


app = FastAPI()

# cors
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


# Endpoints
@app.get("/documents", response_model=list[DocNode])
async def get_documents() -> list[DocNode]:
    """Get all documents from the database.

    Returns:
        List[DocNode]: List of documents
    """
    return list(db.documents_db.values())


@app.post("/generate", response_model=list[tuple[int, float]])
async def generate_scores(query: Query) -> list[tuple[int, float]]:
    """Given a question (query) retrieves the scores for all the documents.

    Scores relates to the cosine similarity between the query and the document.

    Args:
        query (Query): Question to be answered by Oktopus based on your data.

    Returns:
        List[Tuple[int, float]]: List of (doc_id, score) tuples
    """
    # Simulated score generation, returning doc_id and a score
    return [(doc.id, doc.x * 0.5 + doc.y * 0.3) for doc in db.documents_db.values()]


@app.get("/documents/{doc_id}", response_model=Document)
async def get_document_by_id(doc_id: int):
    """Retrieve a document by its id.

    Args:
        doc_id (int): Document id

    Returns:
        Document: Document
    """
    return db.documents_db.get(doc_id)



# frontend
app.mount("/", app=StaticFiles(directory="/static", html=True), name="static")
