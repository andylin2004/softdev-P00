from flask import session           #facilitate user sessions
import sqlite3   #enable control of an sqlite database

DB_FILE="database.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

class AuthService:

    activeUsers = {}

    def __init__(self):
        c.execute("CREATE TABLE IF NOT EXISTS users(ID AUTOINCREMENT PRIMARY KEY, username TEXT,  displayUsername TEXT, password TEXT, UNIQUE (username, ID))")

    def login(self, username, password):
        pass

    def register(self, username, password):
        pass

    def currentUser(self):
        pass
