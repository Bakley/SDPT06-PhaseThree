# Library Management CLI Application

## Description

This is a command-line application for managing a library. It allows you to add, update, list, and soft delete authors, books, members, and loans. It also includes functionality for searching books and checking overdue loans.

## Installation

1. Clone the repository.
2. Navigate to the root directory `loan_library`
3. Install the dependencies using `pip install -r requirements.txt`.
4. Set up the database using `python -c "from db import setup_database; setup_database()"`.

## Usage

Run the CLI using `python cli.py`. Below are the available commands:

### Authors

- `add_author NAME` - Add a new author.
- `list_authors` - List all authors.
- `update_author AUTHOR_ID NAME` - Update an author's name.
- `soft_delete_author AUTHOR_ID` - Soft delete an author.

### Books

- `add_book TITLE AUTHOR_ID GENRE` - Add a new book.
- `list_books` - List all books.
- `update_book BOOK_ID TITLE AUTHOR_ID GENRE` - Update a book's details.
- `soft_delete_book BOOK_ID` - Soft delete a book.
- `search_books KEYWORD` - Search books by title, author, or genre.

### Members

- `add_member NAME EMAIL` - Add a new member.
- `list_members` - List all members.
- `update_member MEMBER_ID NAME EMAIL` - Update a member's details.
- `soft_delete_member MEMBER_ID` - Soft delete a member.

### Loans

- `loan_book BOOK_ID MEMBER_ID` - Loan a book to a member.
- `return_book LOAN_ID` - Return a loaned book.
- `list_loans` - List all loans.
- `check_overdue_books OVERDUE_DATE` - Check for overdue books.

## Contributing

Kindly feel free to submit issues, fork the repository and send pull requests!

## License

This project is licensed under the MIT License.
