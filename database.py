import sqlite3

conn = sqlite3.connect('lessons.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL
)
''')

def add_lesson(title, description):
    cursor.execute('''
        INSERT INTO lessons (title, description) 
        VALUES (?, ?)
    ''', (title, description))
    conn.commit()

def get_all_lessons():
    cursor.execute('SELECT * FROM lessons')
    return cursor.fetchall()

def close_connection():
    conn.close()
