import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from datetime import date
from controller.BDController import DatabaseController
from logic.classes.audiobook import AudioBook
from logic.classes.book import Book
from logic.classes.ebook import Ebook
from logic.classes.invbook import InvBook
from logic.classes.magazine import Magazine


bd_object = DatabaseController()
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"200": "Welcome To Document Restful API"}


@app.get("/api/document/select")
async def root(table_name: str = ''):
    """
    Select all documents from a table
    """
    return bd_object.select_documents(table_name)


@app.post("/api/document/ElectronicDoc/Add/Book")
async def add_book(author: str = "author",
                   title: str = "title",
                   price: float = 100.0,
                   topic: str = "topic",
                   language: str = "language",
                   pub_date: date = date.today(),
                   publisher: str = "publisher",
                   editor: str = "editor",
                   pages: int = 1,
                   synopsis: str = "synopsis",
                   presentation: str = "presentation"):
    """
    Add a book to the database
    """
    return bd_object.insert_document(
        Book(
            author=author,
            title=title,
            price=price,
            topic=topic,
            language=language,
            pub_date=pub_date,
            publisher=publisher,
            editor=editor,
            pages=pages,
            synopsis=synopsis,
            presentation=presentation))


@app.post("/api/document/ElectronicDoc/Add/Audiobook")
async def add_audiobook(author: str = "author",
                        title: str = "title",
                        price: float = 100.0,
                        topic: str = "topic",
                        language: str = "language",
                        pub_date: date = date.today(),
                        size: float = 1,
                        doi: str = "doi",
                        duration: float = 1,
                        synopsis: str = "synopsis"):
    """
    Add an audiobook to the database
    """
    return bd_object.insert_document(
        AudioBook(
            author=author,
            title=title,
            price=price,
            topic=topic,
            language=language,
            pub_date=pub_date,
            size=size,
            doi=doi,
            duration=duration,
            synopsis=synopsis))


@app.post("/api/document/ElectronicDoc/Add/Ebook")
async def add_ebook(author: str = "author",
                    title: str = "title",
                    price: float = 100.0,
                    topic: str = "topic",
                    language: str = "language",
                    pub_date: date = date.today(),
                    size: float = 1,
                    doi: str = "doi",
                    editor: str = "editor",
                    pages: int = 1,
                    synopsis: str = "synopsis"):
    """
    Add an ebook to the database
    """
    return bd_object.insert_document(
        Ebook(
            author=author,
            title=title,
            price=price,
            topic=topic,
            language=language,
            pub_date=pub_date,
            size=size,
            doi=doi,
            editor=editor,
            pages=pages,
            synopsis=synopsis))


@app.post("/api/document/ElectronicDoc/Add/Invbook")
async def add_invbook(author: str = "author",
                      title: str = "title",
                      price: float = 100.0,
                      topic: str = "topic",
                      language: str = "language",
                      pub_date: date = date.today(),
                      size: float = 1,
                      doi: str = "doi",
                      pages: int = 1,
                      abstract: str = "abstract"):
    """
    Add an investigation book to the database
    """
    return bd_object.insert_document(
        InvBook(
            author=author,
            title=title,
            price=price,
            topic=topic,
            language=language,
            pub_date=pub_date,
            size=size,
            doi=doi,
            pages=pages,
            abstract=abstract))


@app.post("/api/document/ElectronicDoc/Add/Magazine")
async def add_magazine(author: str = "author",
                       title: str = "title",
                       price: float = 100.0,
                       topic: str = "topic",
                       language: str = "language",
                       pub_date: date = date.today(),
                       size: float = 1,
                       doi: str = "doi",
                       edition: int = 1,
                       pages: int = 1):
    """
    Add a magazine to the database
    """
    return bd_object.insert_document(
        Magazine(
            author=author,
            title=title,
            price=price,
            topic=topic,
            language=language,
            pub_date=pub_date,
            size=size,
            doi=doi,
            edition=edition,
            pages=pages))


@app.delete("/api/document/delete/{id_document}/{table_name}")
async def delete(id_document: int, table_name: str):
    """
    Delete a document from a table
    """
    if table_name == "Books":
        return bd_object.delete_document(id_document, table_name)
    elif table_name == "Audiobooks":
        return bd_object.delete_document(id_document, table_name)
    elif table_name == "Ebooks":
        return bd_object.delete_document(id_document, table_name)
    elif table_name == "Investigation_books":
        return bd_object.delete_document(id_document, table_name)
    elif table_name == "Magazines":
        return bd_object.delete_document(id_document, table_name)
    else:
        return "Table not found"


if __name__ == "__main__":
    uvicorn.run(app)
