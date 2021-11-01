from flask import session           #facilitate user sessions

class AuthService:

    activeUsers = {}

    def __init__(self):
        c.execute("CREATE TABLE IF NOT EXISTS users(ID AUTOINCREMENT PRIMARY KEY, username TEXT,  displayUsername TEXT, password TEXT, UNIQUE (username, ID))")

    def login(self, username, password):
        pass

    def register(self, username, password):
        c.execute("INSERT INTO users VALUES(? , ?)", username, password)

    def currentUser(self):
        pass
