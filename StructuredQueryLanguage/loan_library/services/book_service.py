from repositories.book_repository import BookRepository

class BookService:

    def __init__(self) -> None:
        self.repo = BookRepository()

    def add_book(self, title, author_id, genre):
        self.repo.add_book(title, author_id, genre)

    def list_books(self):
        return self.repo.list_books()
    
    def update_book(self, book_id, title, author_id, genre):
        self.repo.update_book(book_id, title, author_id, genre)

    def delete_book(self, book_id):
        self.repo.soft_delete_book(book_id)

    def search_book(self, keyword):
        return self.repo.search_books(keyword)
