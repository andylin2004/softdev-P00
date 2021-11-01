from flask import session           #facilitate user sessions
from utils.database import initializeUsersTable();

class AuthService:

    activeUsers = {}

    def __init__(self):
        initializeUsersTable();

    def login(self, username, password):
        pass

    def register(self, username, password):
        c.execute("INSERT INTO users VALUES(? , ?)", username, password)

    def currentUser(self):
        pass
