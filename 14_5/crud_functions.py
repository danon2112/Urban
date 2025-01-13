import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Products (
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT 
    )
    '''
)

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Users (
    id INT PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT 
    )
    '''
)

connection.commit()

# cursor.execute("INSERT INTO Products ('title', 'description', 'price') VALUES ('Товар1', '1', 100)")
# cursor.execute("INSERT INTO Products ('title', 'description', 'price') VALUES ('Товар2', '2', 200)")
# cursor.execute("INSERT INTO Products ('title', 'description', 'price') VALUES ('Товар3', '3', 300)")
# cursor.execute("INSERT INTO Products ('title', 'description', 'price') VALUES ('Товар4', '4', 400)")
# cursor.execute("INSERT INTO Products ('title', 'description', 'price') VALUES ('Товар5', '5', 500)")
# cursor.execute("INSERT INTO Products ('title', 'description', 'price') VALUES ('Товар6', '6', 600)")
# connection.commit()

def get_all_products():
    cursor.execute("SELECT * FROM Products")
    return cursor.fetchall()

def add_user(username, email, age, balance=1000):
    cursor.execute("INSERT INTO Users ('username', 'email', 'age', 'balance') VALUES (?, ?, ?, ?, ?)", (username, email, age, balance))
    connection.commit()

def is_included(username):
    user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,)).fetchone()
    return True if user is not None else False
