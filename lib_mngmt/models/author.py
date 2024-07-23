from main import BaseModel

class Author(BaseModel):
    table_name = 'authors'
    columns = {
        'name': 'TEXT',
        'birth_date': 'TEXT'
    }

    def __init__(self, name, birth_date) -> None:
        self.name = name
        self.birth_date = birth_date

    def __str__(self) -> str:
        return f"Author: {self.name}"
    
    @classmethod
    def find_by_name(cls, name):
        return cls.filter(name=name)
    
    @classmethod
    def find_by_birth_date(cls, birth_date):
        return cls.filter(birth_date=birth_date)
