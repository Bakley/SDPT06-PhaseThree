INSERT INTO authors (name) VALUES (?);

SELECT * FROM authors WHERE deleted = 0;

UPDATE authors SET name = ? WHERE id = ?;

UPDATE authors SET deleted = 1 WHERE id = ?;

INSERT INTO books (title, author_id, genre) VALUES (?, ?, ?);

SELECT * FROM books WHERE deleted = 0;

UPDATE books SET title = ?, author_id = ?, genre = ? WHERE id = ?;

UPDATE books SET deleted = 1 WHERE id = ?;

SELECT books.id, books.title, authors.name, books.genre
FROM books
JOIN authors ON books.author_id = author.id 
WHERE books.deleted = 0 AND authors.deleted = 0
 AND (books.title LIKE '%' || ? '%'
  OR authors.name LIKE '%' || ? '%'
  OR books.genre LIKE '%' || ? '%');

INSERT INTO members (name, email, join_date) VALUES (?, ?, ?);

SELECT * FROM members WHERE deleted = 0;

UPDATE members SET name = ?, email = ? WHERE id = ?;

UPDATE members SET deleted = 1 WHERE id = ?;

INSERT INTO loans (book_id, member_id, loan_date) VALUES (?, ?, ?);

UPDATE loans SET return_date = ? WHERE id = ?;

SELECT * FROM loans WHERE deleted = 0;

SELECT loans.id, books.title, members.name, loans.loan_date
FROM loans
JOIN books ON loans.book_id = books.id 
JOIN members on loans.member_id = members.id 
WHERE loans.deleted = 0 AND books.deleted = 0 AND members.deleted = 0
 AND loans.return_date IS NULL AND loans.loan_date < ?;
