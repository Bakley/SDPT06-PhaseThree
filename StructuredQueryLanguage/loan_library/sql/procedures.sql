-- Stored Procedures
-- Add author
CREATE PROCEDURE IF NOT EXISTS AddAuthor(name TEXT)
BEGIN
    INSERT INTO authors (name) VALUES (name);
END;

-- List all authors
CREATE PROCEDURE IF NOT EXISTS ListAuthors()
BEGIN
    SELECT * FROM authors;
END;

-- Add book
CREATE PROCEDURE IF NOT EXISTS AddBook(title TEXT, author_id INTEGER, genre TEXT)
BEGIN
    INSERT INTO books (title, author_id, genre) VALUES (title, author_id, genre);
END;

-- List all books
CREATE PROCEDURE IF NOT EXISTS ListBooks()
BEGIN
    SELECT * FROM books;
END;

-- Search books
CREATE PROCEDURE IF NOT EXISTS SearchBooks(keyword TEXT)
BEGIN
    SELECT books.id, books.title, authors.name, books.genre
    FROM books
    JOIN authors ON books.author_id = authors.id
    WHERE books.title LIKE '%' || keyword || '%' 
       OR authors.name LIKE '%' || keyword || '%' 
       OR books.genre LIKE '%' || keyword || '%';
END;

-- Add member
CREATE PROCEDURE IF NOT EXISTS AddMember(name TEXT, email TEXT, join_date DATE)
BEGIN
    INSERT INTO members (name, email, join_date) VALUES (name, email, join_date);
END;

-- List all members
CREATE PROCEDURE IF NOT EXISTS ListMembers()
BEGIN
    SELECT * FROM members;
END;

-- Loan book
CREATE PROCEDURE IF NOT EXISTS LoanBook(book_id INTEGER, member_id INTEGER, loan_date DATE)
BEGIN
    INSERT INTO loans (book_id, member_id, loan_date) VALUES (book_id, member_id, loan_date);
END;

-- Return book
CREATE PROCEDURE IF NOT EXISTS ReturnBook(loan_id INTEGER, return_date DATE)
BEGIN
    UPDATE loans SET return_date = return_date WHERE id = loan_id;
END;

-- List all loans
CREATE PROCEDURE IF NOT EXISTS ListLoans()
BEGIN
    SELECT * FROM loans;
END;

-- Check overdue books
CREATE PROCEDURE IF NOT EXISTS CheckOverdueBooks(overdue_date DATE)
BEGIN
    SELECT loans.id, books.title, members.name, loans.loan_date
    FROM loans
    JOIN books ON loans.book_id = books.id
    JOIN members ON loans.member_id = members.id
    WHERE loans.return_date IS NULL AND loans.loan_date < overdue_date;
END;
