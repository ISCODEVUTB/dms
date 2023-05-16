import sqlite3

from logic.classes.audiobook import AudioBook
from logic.classes.book import Book
from logic.classes.ebook import Ebook
from logic.classes.invbook import InvBook
from logic.classes.magazine import Magazine

DATABASE = 'Inventory.sqlite'
INSERT_SUCCESS = "Document inserted successfully"
DELETE_SUCCESS = "Document deleted successfully"


class DatabaseController():
    """
    This class is used to connect to the database and execute queries
    """

    def __init__(self):
        """
        Constructor
        """
        self.connection = sqlite3.connect(DATABASE)
        self.cursor = self.connection.cursor()

    def insert_document(self, document: Book or Ebook or Magazine or AudioBook or InvBook):
        """
        This method is used to insert a document into the database
        """

        self.connection = sqlite3.connect(DATABASE)
        self.cursor = self.connection.cursor()

        if isinstance(document, AudioBook):
            self.cursor.execute('INSERT INTO Audiobooks (author, title, price, topic, language, pub_date, size, doi, duration, synopsis) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi, document.duration, document.synopsis))
            self.connection.commit()
            self.connection.close()

            return INSERT_SUCCESS

        elif isinstance(document, Ebook):
            self.cursor.execute('INSERT INTO Ebooks (author, title, price, topic, language, pub_date, size, doi, editor, pages, synopsis) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi, document.editor, document.pages, document.synopsis))
            self.connection.commit()
            self.connection.close()

            return INSERT_SUCCESS

        elif isinstance(document, Magazine):
            self.cursor.execute('INSERT INTO Magazines ( author, title, price, topic, language, pub_date, size, doi, edition, pages) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi, document.edition, document.pages))
            self.connection.commit()
            self.connection.close()

            return INSERT_SUCCESS

        elif isinstance(document, InvBook):
            self.cursor.execute('INSERT INTO Investigation_books (author, title, price, topic, language, pub_date, size, doi, pages, abstract) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi, document.pages, document.abstract))
            self.connection.commit()
            self.connection.close()

            return INSERT_SUCCESS

        elif isinstance(document, Book):
            self.cursor.execute('INSERT INTO Books (author, title, price, topic, language, pub_date, publisher, editor, pages, synopsis, presentation) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.publisher, document.editor, document.pages, document.synopsis, document.presentation))
            self.connection.commit()
            self.connection.close()

            return INSERT_SUCCESS

    def delete_document(self, id_document: int, table_name: str):
        """
        This method is used to delete a document from the database
        """
        self.connection = sqlite3.connect(DATABASE)
        self.cursor = self.connection.cursor()

        if table_name == "Audiobooks":
            self.cursor.execute(
                '''DELETE FROM Audiobooks WHERE ID = ?''', (id_document,))
            self.connection.commit()
            self.connection.close()
            return DELETE_SUCCESS

        elif table_name == "Ebooks":
            self.cursor.execute(
                '''DELETE FROM Ebooks WHERE ID = ?''', (id_document,))
            self.connection.commit()
            self.connection.close()
            return DELETE_SUCCESS

        elif table_name == "Magazines":
            self.cursor.execute(
                '''DELETE FROM Magazines WHERE ID = ?''', (id_document,))
            self.connection.commit()
            self.connection.close()
            return DELETE_SUCCESS

        elif table_name == "Investigation_books":
            self.cursor.execute(
                '''DELETE FROM Investigation_books WHERE ID = ?''', (id_document,))
            self.connection.commit()
            self.connection.close()
            return DELETE_SUCCESS

        elif table_name == "Books":
            self.cursor.execute(
                '''DELETE FROM Books WHERE ID = ?''', (id_document,))
            self.connection.commit()
            self.connection.close()
            return DELETE_SUCCESS

        else:
            return "Document not found"

    def select_documents(self, table_name: str):
        """
        This method is used to select all documents from the database
        """
        self.connection = sqlite3.connect(DATABASE)
        self.cursor = self.connection.cursor()
        try:
            if table_name == "":
                self.cursor.execute('SELECT * FROM Books')
                rows = self.cursor.fetchall()
                self.cursor.execute('SELECT * FROM Ebooks')
                rows += self.cursor.fetchall()
                self.cursor.execute('SELECT * FROM Audiobooks')
                rows += self.cursor.fetchall()
                self.cursor.execute('SELECT * FROM Magazines')
                rows += self.cursor.fetchall()
                self.cursor.execute('SELECT * FROM Investigation_books')
                rows += self.cursor.fetchall()
                self.connection.commit()
                self.connection.close()
                return rows
            else:
                self.cursor.execute(
                    '''SELECT * FROM {}'''.format(table_name))
                rows = self.cursor.fetchall()
                self.connection.commit()
                self.connection.close()
                return rows
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)


if __name__ == "__main__":
    db = DatabaseController()
