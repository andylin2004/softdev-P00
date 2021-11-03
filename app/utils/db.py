import sqlite3   #enable control of an sqlite database

DB_FILE="database.db"

db = sqlite3.connect(DB_FILE, check_same_thread=False) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

def initializeUsersTable():
    c.execute('''CREATE TABLE IF NOT EXISTS users(
    ID INTEGER PRIMARY KEY,
    username TEXT,
    displayName TEXT,
    password TEXT,
    UNIQUE (username, ID))''')

def initializePostsTable():
    c.execute('''CREATE TABLE IF NOT EXISTS users(
    ID INTEGER PRIMARY KEY,
    author TEXT,
    date TEXT,
    title TEXT,
    content TEXT,
    UNIQUE (ID))''')

def initializeDatabase():
    initializeUsersTable()
    initializePostsTable()

# AUTH
def addUser(username, displayName, password):
    c.execute("INSERT INTO users (username, displayName, password) VALUES(? , ?, ?)", (username, displayName, password))
    db.commit()

def getUserByUsername(username):
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    data = c.fetchone()
    return data

# BLOG MANAGEMENT

def search(searchQuery):
    c.execute("SELECT * FROM blogs WHERE blogTitle LIKE '%:title%'", {'title': searchQuery})
    data = c.fetchall()

def pullUserData(userID):
    c.execute("SELECT * FROM blogs WHERE author IS ':userID'", {'userId': userID})
    data = c.fetchall()

def createBlogPost(title, content, userID):
    c.execute('INSERT INTO blogs VALUES (SELECT COUNT(*) FROM blog, ":userID", SELECT datetime(\'now\'), ":title", ":content")', {'userID': userID, 'title': title, 'content': content})

def loadHomePage():
    c.execute("SELECT * FROM blogs ORDERED BY date DESC")