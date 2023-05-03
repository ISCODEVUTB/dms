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

            self.cursor.execute('INSERT INTO All_documents (author, title, price, topic, language, pub_date) VALUES (?, ?, ?, ?, ?, ?)',
                                (document.author, document.title, document.price, document.topic, document.language, document.pub_date))

            Prev_ID = self.cursor.lastrowid

            self.cursor.execute('INSERT INTO Audiobooks (ID, duration, synopsis) VALUES (?, ?, ?)',
                                (Prev_ID, document.duration, document.synopsis))

            self.cursor.execute('INSERT INTO Electronic_documents (ID,author, title, price, topic, language, pub_date, size, doi) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (Prev_ID, document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi))
            self.connection.commit()

            return "Document inserted successfully"

        elif isinstance(document, Ebook):

            self.cursor.execute('INSERT INTO All_documents (author, title, price, topic, language, pub_date) VALUES (?, ?, ?, ?, ?, ?)',
                                (document.author, document.title, document.price, document.topic, document.language, document.pub_date))

            Prev_ID = self.cursor.lastrowid

            self.cursor.execute('INSERT INTO Ebooks (ID, editor, pages, synopsis) VALUES (?, ?, ?, ?)',
                                (Prev_ID, document.editor, document.pages, document.synopsis))

            self.cursor.execute('INSERT INTO Electronic_documents (ID, author, title, price, topic, language, pub_date, size, doi) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (Prev_ID, document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi))
            self.connection.commit()

            return "Document inserted successfully"

        elif isinstance(document, Magazine):

            self.cursor.execute('INSERT INTO All_documents (author, title, price, topic, language, pub_date) VALUES (?, ?, ?, ?, ?, ?)',
                                (document.author, document.title, document.price, document.topic, document.language, document.pub_date))

            Prev_ID = self.cursor.lastrowid

            self.cursor.execute('INSERT INTO Magazines (ID, edition, pages) VALUES (?, ?, ?)',
                                (Prev_ID, document.edition, document.pages))

            self.cursor.execute('INSERT INTO Electronic_documents (ID, author, title, price, topic, language, pub_date, size, doi) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (Prev_ID, document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi))
            self.connection.commit()

            return "Document inserted successfully"

        elif isinstance(document, InvBook):

            self.cursor.execute('INSERT INTO All_documents (author, title, price, topic, language, pub_date) VALUES (?, ?, ?, ?, ?, ?)',
                                (document.author, document.title, document.price, document.topic, document.language, document.pub_date))

            Prev_ID = self.cursor.lastrowid

            self.cursor.execute('INSERT INTO Investigation_books (ID, pages, abstract) VALUES (?, ?, ?)',
                                (Prev_ID, document.pages, document.abstract))

            self.cursor.execute('INSERT INTO Electronic_documents (ID, author, title, price, topic, language, pub_date, size, doi) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (Prev_ID, document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi))
            self.connection.commit()

            return "Document inserted successfully"

        elif isinstance(document, Book):
            self.cursor.execute('INSERT INTO All_documents (author, title, price, topic, language, pub_date) VALUES (?, ?, ?, ?, ?, ?)',
                                (document.author, document.title, document.price, document.topic, document.language, document.pub_date))

            Prev_ID = self.cursor.lastrowid

            self.cursor.execute('INSERT INTO Books (ID, editor, pages, synopsis, presentation) VALUES (?, ?, ?, ?, ?)',
                                (Prev_ID, document.editor, document.pages, document.synopsis, document.presentation))

            self.cursor.execute('INSERT INTO Physical_documents (ID,author, title, price, topic, language, pub_date, publisher) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                                (Prev_ID, document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.publisher))
            self.connection.commit()

            return "Document inserted successfully"

    def delete_document(self, ID_document: int):

        self.cursor.execute(
            'DELETE FROM Audiobooks WHERE ID = ?', (ID_document,))
        self.cursor.execute('DELETE FROM Ebooks WHERE ID = ?', (ID_document,))
        self.cursor.execute(
            'DELETE FROM Investigation_books WHERE ID = ?', (ID_document,))
        self.cursor.execute(
            'DELETE FROM Magazines WHERE ID = ?', (ID_document,))
        self.cursor.execute('DELETE FROM Books WHERE ID = ?', (ID_document,))

        self.cursor.execute(
            'DELETE FROM Electronic_documents WHERE ID = ?', (ID_document,))
        self.cursor.execute(
            'DELETE FROM Physical_documents WHERE ID = ?', (ID_document,))

        self.cursor.execute(
            'DELETE FROM All_documents WHERE ID = ?', (ID_document,))

        self.connection.commit()
        return "Document deleted successfully"

    def select_documents(self):
        self.cursor.execute('''SELECT * FROM All_documents''')
        return self.cursor.fetchall()


if __name__ == "__main__":
    db = DatabaseController()
