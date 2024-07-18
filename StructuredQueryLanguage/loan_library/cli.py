import click
from datetime import date
from services.author_service import AuthorService
from services.book_service import BookService
from services.member_service import MemberService
from services.loan_service import LoanService

author_service = AuthorService()
book_service = BookService()
member_service = MemberService()
loan_service = LoanService()


@click.group()
def cli():
    """Library Management System"""
    pass

@click.command()
@click.argument('name')
def add_author(name):
    """Add a new author record"""
    author_service.add_author(name)
    click.echo(f'Author "{name} added"')

@click.command()
def list_authors():
    click.echo('Listing all authors.')
    authors = author_service.list_authors()
    # import pdb; pdb.set_trace()
    for author in authors:
        click.echo(f'ID: {author[0]}, Name: {author[1]}')

@cli.command()
@click.argument('author_id', type=int)
@click.argument('name')
def update_author(author_id, name):
    """Update an author"""
    author_service.update_author(author_id, name)
    click.echo(f'Author with ID {author_id} updated.')

@cli.command()
@click.argument('author_id', type=int)
def soft_delete_author(author_id):
    """Soft delete an author"""
    author_service.delete_author(author_id)
    click.echo(f'Author with ID {author_id} deleted.')

# Book CRUD cli functions
@click.command()
@click.argument('title')
@click.argument('author_id', type=int)
@click.argument('genre')
def add_book(title, author_id, genre):
    """Add a new book record"""
    book_service.add_book(title, author_id, genre)
    click.echo(f'Book "{title} added"')

@cli.command()
def list_books():
    """List all books"""
    books = book_service.list_books()
    for book in books:
        click.echo(f'ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}, Genre: {book[3]}')

@cli.command()
@click.argument('book_id', type=int)
@click.argument('title')
@click.argument('author_id', type=int)
@click.argument('genre')
def update_book(book_id, title, author_id, genre):
    """Update a book"""
    book_service.update_book(book_id, title, author_id, genre)
    click.echo(f'Book with ID {book_id} updated.')

@cli.command()
@click.argument('book_id', type=int)
def soft_delete_book(book_id):
    """Soft delete a book"""
    book_service.soft_delete_book(book_id)
    click.echo(f'Book with ID {book_id} deleted.')

@cli.command()
@click.argument('keyword')
def search_books(keyword):
    """Search books by keyword"""
    books = book_service.search_books(keyword)
    for book in books:
        click.echo(f'ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}')

# Member CRUD cli functions

@cli.command()
@click.argument('name')
@click.argument('email')
def add_member(name, email):
    """Add a new member"""
    join_date = date.today().isoformat()
    member_service.add_member(name, email, join_date)
    click.echo(f'Member "{name}" added.')

@cli.command()
def list_members():
    """List all members"""
    members = member_service.list_members()
    for member in members:
        click.echo(f'ID: {member[0]}, Name: {member[1]}, Email: {member[2]}, Join Date: {member[3]}')

@cli.command()
@click.argument('member_id', type=int)
@click.argument('name')
@click.argument('email')
def update_member(member_id, name, email):
    """Update a member"""
    member_service.update_member(member_id, name, email)
    click.echo(f'Member with ID {member_id} updated.')

@cli.command()
@click.argument('member_id', type=int)
def soft_delete_member(member_id):
    """Soft delete a member"""
    member_service.soft_delete_member(member_id)
    click.echo(f'Member with ID {member_id} deleted.')

# Loan CRUD cli functions

@cli.command()
@click.argument('book_id', type=int)
@click.argument('member_id', type=int)
def loan_book(book_id, member_id):
    """Loan a book to a member"""
    loan_date = date.today().isoformat()
    loan_service.loan_book(book_id, member_id, loan_date)
    click.echo(f'Book with ID {book_id} loaned to member with ID {member_id}.')

@cli.command()
@click.argument('loan_id', type=int)
def return_book(loan_id):
    """Return a loaned book"""
    return_date = date.today().isoformat()
    loan_service.return_book(loan_id, return_date)
    click.echo(f'Loan with ID {loan_id} has been returned.')

@cli.command()
def list_loans():
    """List all loans"""
    loans = loan_service.list_loans()
    for loan in loans:
        click.echo(f'ID: {loan[0]}, Book ID: {loan[1]}, Member ID: {loan[2]}, Loan Date: {loan[3]}, Return Date: {loan[4]}')

@cli.command()
@click.argument('overdue_date')
def check_overdue_books(overdue_date):
    """Check for overdue books"""
    loans = loan_service.check_overdue_books(overdue_date)
    for loan in loans:
        click.echo(f'Loan ID: {loan[0]}, Book: {loan[1]}, Member: {loan[2]}, Loan Date: {loan[3]}')

# Add commands to the CLI group
cli.add_command(add_author)
cli.add_command(list_authors)
cli.add_command(update_author)
cli.add_command(soft_delete_author)

cli.add_command(add_book)
cli.add_command(list_books)
cli.add_command(search_books)
cli.add_command(add_member)
cli.add_command(list_members)
cli.add_command(loan_book)
cli.add_command(return_book)
cli.add_command(list_loans)
cli.add_command(check_overdue_books)
if __name__ == "__main__":
    cli()
    