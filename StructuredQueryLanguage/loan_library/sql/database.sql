--Schema definition
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    deleted INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER, -- Store the author id
    genre TEXT,
    deleted INTEGER DEFAULT 0,
    FOREIGN KEY (author_id) REFERENCES authors(id) -- Create a relationship
);

CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    join_date DATE NOT NULL,
    deleted INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS loans (
    id INTEGER PRIMARY KEY,
    book_id INTEGER,
    member_id INTEGER,
    loan_date DATE NOT NULL,
    return_date DATE,
    deleted INTEGER DEFAULT 0,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (member_id) REFERENCES members(id)
);
