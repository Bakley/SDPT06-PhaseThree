from main import BaseModel
from .author import Author

class Book(BaseModel):
    table_name = 'books'
    columns = {
        'title': 'TEXT',
        'author_id': 'INTEGER',
        'published_date': 'TEXT',
        'available': 'BOOLEAN DEFAULT 1'
    }

    def __init__(self, title, author_id, published_date):
        self.title = title
        self.author_id = author_id
        self.published_date = published_date
        self.available = True

    def __str__(self):
        return f"Book: {self.title}, Author ID: {self.author_id}, Published Date: {self.published_date}, Available: {self.available}"

    def update_title(self, new_title):
        self.title = new_title
        self.update(title=new_title)

    def get_age(self):
        from datetime import datetime
        published_date = datetime.fromisoformat(self.published_date)
        today = datetime.now()
        return today.year - published_date.year - ((today.month, today.day) < (published_date.month, published_date.day))

    @classmethod
    def find_by_title(cls, title):
        return cls.filter(title=title)

    @classmethod
    def find_by_author(cls, author_id):
        return cls.filter(author_id=author_id)

    @classmethod
    def get_author(cls, book_id):
        book = cls.get(book_id)
        author = Author.get(book['author_id'])
        return author

    def mark_as_unavailable(self):
        self.available = False
        self.update(available=False)
    
    def mark_as_available(self):
        self.available = True
        self.update(available=True)
