import json
from time import monotonic

from pydantic import BaseModel
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

from scripts.const import PATH_DATA, QDRANT_COLL_NAME, QDRANT_LOCAL_PATH, MODEL_NAME


class DocumentPosition(BaseModel):
    id: int
    x: float
    y: float
    title: str
    chunk: str


class DocumentScore(DocumentPosition):
    score: float


class Document(DocumentPosition):
    content: str


def _qdrant_payload_to_score(qdrant_response) -> DocumentScore:
    id = qdrant_response.payload['doc_id']
    x = qdrant_response.payload['doc_id']
    y = qdrant_response.payload['doc_id']
    title = qdrant_response.payload['title']
    chunk = qdrant_response.payload['chunk']
    score = qdrant_response.score

    return DocumentScore(id=id, x=x, y=y, title=title, score=score, chunk=chunk)


def search_in_qdrant(text: str, model: SentenceTransformer, client: QdrantClient, limit: int) -> list[DocumentPosition]:
    tic = monotonic()

    response_search = client.search(
        collection_name=QDRANT_COLL_NAME,
        query_vector=model.encode(text),
        limit=limit,
    )
    print(f"query took {monotonic() - tic:.2f}")

    return [_qdrant_payload_to_score(qdrant_response) for qdrant_response in response_search]


if __name__ == "__main__":
    qa_doc = list(PATH_DATA.glob("*.json"))[0]
    qa_test = json.loads(qa_doc.read_text())

    model = SentenceTransformer(MODEL_NAME)
    client = QdrantClient(path=QDRANT_LOCAL_PATH)
    responses = []
    for qa in qa_test:
        question = qa['question']
        docs_position = search_in_qdrant(question, model, client, 5)
        responses.append({'question': question, 'answer': docs_position[0].chunk, 'score': docs_position[0].score})
        responses.append({'question': question, 'answer1': docs_position[1].chunk, 'score1': docs_position[1].score})
        responses.append({'question': question, 'answer2': docs_position[2].chunk, 'score1': docs_position[2].score})


# 1. generar al menos 50-100 documentos
# 2. preparar un caso de uso
# generar más preguntas pequeñas
# 3. probar