from db import execute_query
from utils import get_commands, load_sql_commands

commands = load_sql_commands('sql/stored_procedures.sql')


class AuthorRepository:

    def __init__(self) -> None:
        self.add_author_query = get_commands("INSERT INTO authors", commands)
        self.list_authors_query = get_commands("SELECT * FROM authors WHERE deleted = 0", commands)
        self.update_author_query = get_commands("UPDATE authors SET name", commands)
        self.soft_delete_author_query = get_commands("UPDATE authors SET deleted = 1 WHERE id", commands)
        # self.queries = load_sql_commands('sql/stored_procedures.sql')



    def add_author(self, name):
        execute_query(self.add_author_query, (name,))

    def list_authors(self):
        try:
            return execute_query(self.list_authors_query)
        except Exception as e:
            print(f'Error listing authors: {str(e)}')
            raise

    def update_author(self, author_id, name):
        execute_query(self.update_author_query, (name, author_id))

    def soft_delete_author(self, author_id):
        execute_query(self.soft_delete_author_query, (author_id,))
        