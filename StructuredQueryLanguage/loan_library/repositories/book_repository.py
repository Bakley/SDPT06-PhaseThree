from db import execute_query
from utils import get_commands, load_sql_commands

commands = load_sql_commands('sql/stored_procedures.sql')


class BookRepository:

    def __init__(self) -> None:
        self.add_book_query = get_commands("INSERT INTO books", commands)
        self.list_books_query = get_commands("SELECT * FROM books WHERE deleted = 0", commands)
        self.update_book_query = get_commands("UPDATE books SET title", commands)
        self.soft_delete_book_query = get_commands("UPDATE books SET deleted = 1 WHERE id", commands)
        self.search_books_query = get_commands("SELECT books.id, books.title", commands)


    def add_book(self, title, author_id, genre):
        execute_query(self.add_book_query, (title, author_id, genre,))

    def list_books(self):
        try:
            return execute_query(self.list_books_query)
        except Exception as e:
            print(f'Error listing books: {str(e)}')
            raise

    def update_book(self, book_id, title, author_id, genre):
        execute_query(self.update_book_query, (title, author_id, genre, book_id))

    def soft_delete_book(self, book_id):
        execute_query(self.soft_delete_book_query, (book_id,))
        
    def search_books(self, keyword):
        return execute_query(self.search_books_query,(keyword, keyword, keyword))