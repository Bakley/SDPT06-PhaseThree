from db import execute_query
from utils import get_commands, load_sql_commands

commands = load_sql_commands('sql/stored_procedures.sql')

class LoanRepository:
    def __init__(self):
        self.loan_book_query = get_commands("INSERT INTO loans", commands)
        self.return_book_query = get_commands("UPDATE loans SET return_date", commands)
        self.list_loans_query = get_commands("SELECT * FROM loans WHERE deleted = 0", commands)
        self.soft_delete_loan_query = get_commands("UPDATE loans SET deleted = 1 WHERE id", commands)
        self.check_overdue_books_query = get_commands("SELECT loans.id, books.title", commands)

    def loan_book(self, book_id, member_id, loan_date):
        execute_query(self.loan_book_query, (book_id, member_id, loan_date))

    def return_book(self, loan_id, return_date):
        execute_query(self.return_book_query, (return_date, loan_id))

    def list_loans(self):
        return execute_query(self.list_loans_query)

    def soft_delete_loan(self, loan_id):
        execute_query(self.soft_delete_loan_query, (loan_id,))

    def check_overdue_books(self, overdue_date):
        return execute_query(self.check_overdue_books_query, (overdue_date,))
