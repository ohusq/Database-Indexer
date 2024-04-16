print('This program will delete previous databases and create a new one.')
print('Please make sure to backup your previous databases before proceeding.')
print('Press Enter to continue or Ctrl+C / ^C to exit.')
input()

import sqlite3
import os

# Check if the database file exists
if os.path.exists('credentials.db'):
    os.remove('credentials.db')

db = sqlite3.connect('credentials.db')

cursor = db.cursor() # Create a cursor object to execute SQL commands

# Create a table for storing user information
cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Username TEXT UNIQUE,
                    Password TEXT
                 )''')

# Create indexes for username and password columns
def create_index(cursor, table, column) -> None:
    cursor.execute(f'CREATE INDEX IF NOT EXISTS idx_{column} ON {table} ({column})')


def sort_first_split(line: str) -> tuple:
    parts = line.strip().rsplit(':', 1)
    username = parts[0]
    password = parts[1] if len(parts) > 1 else ''
    return username, password

def add_user(cursor, username: str, password: str) -> None:
    try:
        cursor.execute('INSERT INTO Users (Username, Password) VALUES (?, ?)', (username, password))
        
    except sqlite3.IntegrityError:
        pass # Ignore duplicate entries


def read_file(file_path: str) -> None:
    with open(file_path, 'r') as file:
        for line in file:
            username, password = sort_first_split(line)
            # if username or password doesnt exist, put a space
            if not username:
                username = ' '
            if not password:
                password = ' '
            add_user(cursor, username, password)

    cursor.connection.commit()  # Commit changes to the database

for files in os.listdir('combolists/MailPassword'):
    if files.endswith('.txt'):
        print(f"Reading {files}...")
        read_file(f'combolists/MailPassword/{files}')

for files in os.listdir('combolists/UserPassword'):
    if files.endswith('.txt'):
        print(f"Reading {files}...")
        read_file(f'combolists/UserPassword/{files}')