import sqlite3


connection = sqlite3.connect('not_telegram2.db')
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

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))
cursor.execute('SELECT COUNT(*) FROM Users')
count = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
balance_sum = cursor.fetchone()[0]
print(balance_sum/count)

connection.commit()
connection.close()
