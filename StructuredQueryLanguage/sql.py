# Interaction with the database

# Client sends a request based on user interactions to the server API
# Server API will send a query to the database 

# A database a file that will store clean data and respond to queries 


# SQL
# A standard langague for managing and manipulating relational databases
# 1. CRUD
    # Create => Post - Adding new records
    # Read => Get - Quering database to fetch information
    # Update => Patch or Put - modify existing records
    # Delete => Soft Delete - Removing the relationship between records
# 2. Create and manage schemas = migration and updates


# Tool we might encounter
# # SQLite 
# # SQLALchemy - ORM
# # Psycopg2 - act as a connector[postgresql, mysql]


############# Connect to a database #############
import sqlite3 

# connect to sqlite3 database

conn = sqlite3.connect('myexample.db')

# # Create a cursor object to execute SQL commands

cursor = conn.cursor()

# Create table(if not exists)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
    )
    """
)

# post request => insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Abel', 23))
cursor.execute(
    "INSERT INTO users (name, age) VALUES (?, ?)", ("", 24)
    )
cursor.execute(
    "INSERT INTO users (name, age) VALUES (?, ?)", ('Wassabi', 123)
    )

# Save(commit) the changes
conn.commit()

# Get request => seecting from the table
cursor.execute(
    "SELECT * FROM users"
    )
rows = cursor.fetchall()
for item in rows:
    print(type(item), item)


# Update A Record
cursor.execute(
    "UPDATE users SET age = ? WHERE name = ?", (150, 'Wassabi')
    )
conn.commit()

# Delete a record
cursor.execute(
    "DELETE FROM users WHERE name = ?", ('Abel',)
    )
conn.commit()


# Select data again after modifications
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
