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
async def root():
    return bd_object.select_documents()


@app.post("/api/document/ElectronicDoc/Add/Book")
async def add_Book(author: str = "author", title: str = "title", price: float = 100.0, topic: str = "topic", language: str = "language", pub_date: date = date.today(), publisher: str = "publisher", editor: str = "editor", pages: int = 1, synopsis: str = "synopsis", presentation: str = "presentation"):
    return bd_object.insert_document(Book(author=author, title=title, price=price, topic=topic, language=language, pub_date=pub_date, publisher=publisher, editor=editor, pages=pages, synopsis=synopsis, presentation=presentation))


@app.post("/api/document/ElectronicDoc/Add/Audiobook")
async def add_Audiobook(author: str = "author", title: str = "title", price: float = 100.0, topic: str = "topic", language: str = "language", pub_date: date = date.today(), size: float = 1, doi: str = "doi", duration: float = 1, synopsis: str = "synopsis"):
    return bd_object.insert_document(AudioBook(author=author, title=title, price=price, topic=topic, language=language, pub_date=pub_date, size=size, doi=doi, duration=duration, synopsis=synopsis))


@app.post("/api/document/ElectronicDoc/Add/Ebook")
async def add_Ebook(author: str = "author", title: str = "title", price: float = 100.0, topic: str = "topic", language: str = "language", pub_date: date = date.today(), size: float = 1, doi: str = "doi", editor: str = "editor", pages: int = 1, synopsis: str = "synopsis"):
    return bd_object.insert_document(Ebook(author=author, title=title, price=price, topic=topic, language=language, pub_date=pub_date, size=size, doi=doi, editor=editor, pages=pages, synopsis=synopsis))


@app.post("/api/document/ElectronicDoc/Add/Invbook")
async def add_Invbook(author: str = "author", title: str = "title", price: float = 100.0, topic: str = "topic", language: str = "language", pub_date: date = date.today(), size: float = 1, doi: str = "doi", pages: int = 1, abstract: str = "abstract"):
    return bd_object.insert_document(InvBook(author=author, title=title, price=price, topic=topic, language=language, pub_date=pub_date, size=size, doi=doi, pages=pages, abstract=abstract))


@app.post("/api/document/ElectronicDoc/Add/Magazine")
async def add_Magazine(author: str = "author", title: str = "title", price: float = 100.0, topic: str = "topic", language: str = "language", pub_date: date = date.today(), size: float = 1, doi: str = "doi", edition: int = 1, pages: int = 1):
    return bd_object.insert_document(Magazine(author=author, title=title, price=price, topic=topic, language=language, pub_date=pub_date, size=size, doi=doi, edition=edition, pages=pages))


@app.delete("/api/document/delete/{id_document}/{table_name}")
async def delete(id_document: int, table_name: str):
    if table_name == "Books" or "Audiobooks" or "Ebooks" or "Magazines" or "Investigation_books":
        return bd_object.delete_document(id_document, table_name)
    else:
        return "Table not found"


if __name__ == "__main__":
    uvicorn.run(app, port=33507)
