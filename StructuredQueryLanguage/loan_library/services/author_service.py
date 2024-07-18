# Handles the businnes logic side

from repositories.author_repository import AuthorRepository

class AuthorService:

    def __init__(self) -> None:
        self.repository = AuthorRepository()

    def add_author(self, name):
        self.repository.add_author(name)

    def list_authors(self):
        return self.repository.list_authors()

    def update_author(self, author_id, name):
        self.repository.update_author(author_id, name)

    def delete_author(self, author_id):
        self.repository.soft_delete_author(author_id)
