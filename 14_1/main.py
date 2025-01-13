import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL, age INTEGER, balance INTEGER NOT NULL)')
connection.commit()


for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i}', f'example{i}@gmail.com', i*10, 1000))
connection.commit()



cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

for user in users:
    if user[0] % 2 != 0:
        cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, user[0]))
connection.commit()


for user in users:
    if user[0] % 3 == 1:
        cursor.execute('DELETE FROM Users WHERE id = ?', (user[0],))
connection.commit()



cursor.execute('SELECT * FROM Users WHERE age != 60')
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

connection.close()