from repositories.loan_repository import LoanRepository

class LoanService:
    def __init__(self):
        self.repository = LoanRepository()

    def loan_book(self, book_id, member_id, loan_date):
        self.repository.loan_book(book_id, member_id, loan_date)

    def return_book(self, loan_id, return_date):
        self.repository.return_book(loan_id, return_date)

    def list_loans(self):
        return self.repository.list_loans()

    def soft_delete_loan(self, loan_id):
        self.repository.soft_delete_loan(loan_id)

    def check_overdue_books(self, overdue_date):
        return self.repository.check_overdue_books(overdue_date)
