from db import execute_query
from utils import get_commands, load_sql_commands

commands = load_sql_commands('sql/stored_procedures.sql')


class MemberRepository:

    def __init__(self) -> None:
        self.add_member_query = get_commands("INSERT INTO members", commands)
        self.list_members_query = get_commands("SELECT * FROM members WHERE deleted = 0", commands)
        self.update_member_query = get_commands("UPDATE members SET name", commands)
        self.soft_delete_member_query = get_commands("UPDATE members SET deleted = 1 WHERE id", commands)
        # self.queries = load_sql_commands('sql/stored_procedures.sql')


    def add_member(self, name, email, join_date):
        execute_query(self.add_member_query, (name, email, join_date))

    def list_members(self):
        try:
            return execute_query(self.list_members_query)
        except Exception as e:
            print(f'Error listing members: {str(e)}')
            raise

    def update_member(self, member_id, name, email):
        execute_query(self.update_member_query, (name, email, member_id))

    def soft_delete_member(self, member_id):
        execute_query(self.soft_delete_member_query, (member_id,))
        