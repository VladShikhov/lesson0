import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)               
''')

# заполнение таблицы
# for i in range(10):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i+1}', f'example{i+1}@gmail.com', (i+1)*10, 1000))

# обновление таблицы
# cursor.execute('UPDATE Users SET balance = ? WHERE id % ? != 0', (500, 2))

# удаление каждой 3-й записи из таблицы
count = 1
for i in range(10):
    cursor.execute('DELETE FROM Users WHERE id = ?', (count,))
    count += 3

# выборка пользователей
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
users = cursor.fetchall()
for user in users:
    print(f'{user[0]} | {user[1]} | {user[2]} | {user[3]}')

connection.commit()
connection.close()
