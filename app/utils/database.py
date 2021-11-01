import sqlite3   #enable control of an sqlite database

DB_FILE="database.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

def initializeUsersTable():
    c.execute('''CREATE TABLE IF NOT EXISTS users(
    ID PRIMARY KEY,
    username TEXT,
    displayUsername TEXT,
    password TEXT,
    UNIQUE (username, ID))''')

def initializePostsTable():
    c.execute('''CREATE TABLE IF NOT EXISTS users(
    ID PRIMARY KEY,
    author TEXT,
    date TEXT,
    title TEXT,
    content TEXT,
    UNIQUE (ID))''')

def initializeDatabase():
    initializeUsersTable()
    initializePostsTable()
