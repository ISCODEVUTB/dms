import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
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


@app.get("/api/user")
async def root():
    return bd_object.select_documents()


@app.post("/api/document/ElectronicDoc/Book")
async def add(author="author", title="title", price=100.0, topic="topic", language="language", pub_date="2000-01-01", publisher="publisher", editor="editor", pages=1, synopsis="synopsis", presentation="presentation"):
    return bd_object.insert_document(Book(author=author, title=title, price=price, topic=topic, language=language, pub_date=pub_date, publisher=publisher, editor=editor, pages=pages, synopsis=synopsis, presentation=presentation))


@app.post("/api/document/ElectronicDoc/Audiobook")
async def add(author="author", title="title", price=100.0, topic="topic", language="language", pub_date="2000-01-01", size=1, doi="doi", duration=1, synopsis="synopsis"):
    return bd_object.insert_document(AudioBook(author=author, title=title, price=price, topic=topic, language=language, pub_date=pub_date, size=size, doi=doi, duration=duration, synopsis=synopsis))


@app.post("/api/document/ElectronicDoc/Ebook")
async def add(author="author", title="title", price=100.0, topic="topic", language="language", pub_date="2000-01-01", size=1, doi="doi", editor="editor", pages=1, synopsis="synopsis"):
    return bd_object.insert_document(Ebook(author=author, title=title, price=price, topic=topic, language=language, pub_date=pub_date, size=size, doi=doi, editor=editor, pages=pages, synopsis=synopsis))


@app.post("/api/document/ElectronicDoc/Invbook")
async def add(author="author", title="title", price=100.0, topic="topic", language="language", pub_date="2000-01-01", size=1, doi="doi", pages=1, abstract="abstract"):
    return bd_object.insert_document(InvBook(author=author, title=title, price=price, topic=topic, language=language, pub_date=pub_date, size=size, doi=doi, pages=pages, abstract=abstract))


@app.post("/api/document/ElectronicDoc/Magazine")
async def add(author="author", title="title", price=100.0, topic="topic", language="language", pub_date="2000-01-01", size=1, doi="doi", edition=1, pages=1):
    return bd_object.insert_document(Magazine(author=author, title=title, price=price, topic=topic, language=language, pub_date=pub_date, size=size, doi=doi, edition=edition, pages=pages))


@app.delete("/api/user")
async def delete(id_document: int):
    return bd_object.delete_document(id_document)


if __name__ == "__main__":
    uvicorn.run(app, port=33507)
