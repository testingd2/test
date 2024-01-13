import sqlite3
from datetime import datetime

# Підключення до бази даних (якщо файл не існує, то він буде створений)
conn = sqlite3.connect('temperature_database.txt')

# Створення курсору для виконання SQL-запитів
cursor = conn.cursor()

# Створення таблиці з двома полями: дата_час та температура
cursor.execute('''
    CREATE TABLE IF NOT EXISTS temperature_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_time TEXT NOT NULL,
        temperature REAL NOT NULL
    )
''')

# Збереження змін та закриття підключення
conn.commit()
conn.close()
def insert_temperature(date_time, temperature):
    conn = sqlite3.connect('temperature_database.txt')
    cursor = conn.cursor()

    # Вставка нового рядка із датою, часом та температурою
    cursor.execute('INSERT INTO temperature_data (date_time, temperature) VALUES (?, ?)', (date_time, temperature))

    conn.commit()
    conn.close()

# Внесення даних з датою і часом "17:03" та температурою "-2"
date_time_to_insert = "2024-01-13 17:03:00"
temperature_to_insert = -2.0

insert_temperature(date_time_to_insert, temperature_to_insert)