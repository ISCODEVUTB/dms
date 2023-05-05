import sqlite3

from logic.classes.audiobook import AudioBook
from logic.classes.book import Book
from logic.classes.ebook import Ebook
from logic.classes.invbook import InvBook
from logic.classes.magazine import Magazine


class DatabaseController():

    def __init__(self):
        self.connection = sqlite3.connect('Inventory.sqlite')
        self.cursor = self.connection.cursor()

    def insert_document(self, document: Book or Ebook or Magazine or AudioBook or InvBook):

        if isinstance(document, AudioBook):
            self.cursor.execute('INSERT INTO Audiobooks (author, title, price, topic, language, pub_date, size, doi, duration, synopsis) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi, document.duration, document.synopsis))
            self.connection.commit()

            return "Document inserted successfully"

        elif isinstance(document, Ebook):
            self.cursor.execute('INSERT INTO Ebooks (author, title, price, topic, language, pub_date, size, doi, editor, pages, synopsis) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi, document.editor, document.pages, document.synopsis))
            self.connection.commit()

            return "Document inserted successfully"

        elif isinstance(document, Magazine):
            self.cursor.execute('INSERT INTO Magazines ( author, title, price, topic, language, pub_date, size, doi, edition, pages) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi, document.edition, document.pages))
            self.connection.commit()

            return "Document inserted successfully"

        elif isinstance(document, InvBook):
            self.cursor.execute('INSERT INTO Investigation_books (author, title, price, topic, language, pub_date, size, doi, pages, abstract) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi, document.pages, document.abstract))
            self.connection.commit()

            return "Document inserted successfully"

        elif isinstance(document, Book):
            self.cursor.execute('INSERT INTO Books (author, title, price, topic, language, pub_date, publisher, editor, pages, synopsis, presentation) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.publisher, document.editor, document.pages, document.synopsis, document.presentation))
            self.connection.commit()

            return "Document inserted successfully"

    def delete_document(self, ID_document: int, table_name: str):

        if table_name == "Audiobooks":
            self.cursor.execute(
                '''DELETE FROM Audiobooks WHERE ID = ?''', (ID_document,))
            self.connection.commit()
            return "Document deleted successfully"

        elif table_name == "Ebooks":
            self.cursor.execute(
                '''DELETE FROM Ebooks WHERE ID = ?''', (ID_document,))
            self.connection.commit()
            return "Document deleted successfully"

        elif table_name == "Magazines":
            self.cursor.execute(
                '''DELETE FROM Magazines WHERE ID = ?''', (ID_document,))
            self.connection.commit()
            return "Document deleted successfully"

        elif table_name == "Investigation_books":
            self.cursor.execute(
                '''DELETE FROM Investigation_books WHERE ID = ?''', (ID_document,))
            self.connection.commit()
            return "Document deleted successfully"

        elif table_name == "Books":
            self.cursor.execute(
                '''DELETE FROM Books WHERE ID = ?''', (ID_document,))
            self.connection.commit()
            return "Document deleted successfully"

        else:
            return "Document not found"

    def select_documents(self):
        self.cursor.execute(
            '''SELECT * FROM Books, Audiobooks, Ebooks, Magazines, Investigation_books''')

        return self.cursor.fetchall()


if __name__ == "__main__":
    db = DatabaseController()
