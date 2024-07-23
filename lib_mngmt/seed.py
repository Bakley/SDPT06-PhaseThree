import random

from datetime import datetime, timedelta
from models.author import Author
from models.book import Book

def random_date(start, end):
    return start + (end - start) * random.random()

def seed_data():
    #Seed Authors

    for _ in range(42):
        author = Author(
            name = random.choice(['John', 'Jane', 'Alice', 'Bob', 'Charlie']),
            birth_date=random_date(datetime(1920, 1, 1), datetime(2024, 7, 23)).isoformat()
        )

        author.save()


    #seed Books
    author_ids = [author.id for author in Author.all()]

    for _ in range(42):
        book = Book(
            title="",
            author_id=random.choice(author_ids),
            published_date=(datetime(1950, 1, 1), datetime(2020, 12, 31)).isoformat()
        )

        book.save()

if __name__ == "__main__":
    seed_data()
    