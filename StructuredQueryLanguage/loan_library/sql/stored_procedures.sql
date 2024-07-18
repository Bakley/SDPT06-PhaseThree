-- Add Author
INSERT INTO authors (name) VALUES (?);

-- List all authors
SELECT * FROM authors WHERE deleted = 0;

--Update author
UPDATE authors SET name = ? WHERE id = ?;

--Soft delete author
UPDATE authors SET deleted = 1 WHERE id = ?;

-- Add book
INSERT INTO books (title, author_id, genre) VALUES (?, ?, ?);

-- List all books
SELECT * FROM books WHERE deleted = 0;

-- Update book
UPDATE books SET title = ?, author_id = ?, genre = ? WHERE id = ?;

-- Soft delete book
UPDATE books SET deleted = 1 WHERE id = ?;

-- Search books
SELECT books.id, books.title, authors.name, books.genre
FROM books
JOIN authors ON books.author_id = author.id 
WHERE books.deleted = 0 AND authors.deleted = 0
 AND (books.title LIKE '%' || ? '%'
  OR authors.name LIKE '%' || ? '%'
  OR books.genre LIKE '%' || ? '%');

-- Add member
INSERT INTO members (name, email, join_date) VALUES (?, ?, ?);

-- List all members
SELECT * FROM members WHERE deleted = 0;

-- Update member
UPDATE members SET name = ?, email = ? WHERE id = ?;

-- Soft delete member
UPDATE members SET deleted = 1 WHERE id = ?;

-- Loan book
INSERT INTO loans (book_id, member_id, loan_date) VALUES (?, ?, ?);

-- Return book
UPDATE loans SET return_date = ? WHERE id = ?;

-- List all loans
SELECT * FROM loans WHERE deleted = 0;

-- Check overdue books
SELECT loans.id, books.title, members.name, loans.loan_date
FROM loans
JOIN books ON loans.book_id = books.id 
JOIN members on loans.member_id = members.id 
WHERE loans.deleted = 0 AND books.deleted = 0 AND members.deleted = 0
 AND loans.return_date IS NULL AND loans.loan_date < ?;
