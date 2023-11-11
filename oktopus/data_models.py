"""Data models for the Oktopus API."""
from pydantic import BaseModel


# Define data structures
class DocNode(BaseModel):
    """Represents a document in the graph.

    Attributes:
        id (int): Document id
        x (float): x coordinate
        y (float): y coordinate
        title (str): Document title
    """

    id: int
    x: float
    y: float
    title: str


class Document(DocNode):
    """Represents a real document.

    Attributes:
        content (str): Document content
    """

    content: str


class Query(BaseModel):
    """Question to be answered by Oktopus.

    Attributes:
        query (str): Query
    """

    query: str


class DocumentScore(DocNode):
    score: float
    chunk: str
