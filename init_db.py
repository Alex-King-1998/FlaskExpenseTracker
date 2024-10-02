import sqlite3

connection = sqlite3.connect('expenses.db')
cursor = connection.cursor()

# Create the expenses table
cursor.execute('''
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    amount REAL NOT NULL
)
''')

connection.commit()
connection.close()
