"""Functions to interact with the database."""

from oktopus.data_models import Document

# Simulated database
documents_db = {
    1: Document(
        id=1,
        x=0.5,
        y=0.7,
        title="Document 1",
        content="Content of Document 1",
    ),
    2: Document(
        id=2,
        x=0.8,
        y=0.2,
        title="Document 2",
        content="Content of Document 2",
    ),
}
