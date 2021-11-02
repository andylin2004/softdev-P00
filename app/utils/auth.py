from flask import session           #facilitate user sessions
from utils.db import initializeUsersTable, addUser;

class AuthService:

    activeUsers = {}

    def __init__(self):
        initializeUsersTable()

    def login(self, username, password):
        pass

    def register(self, username, displayName, password):
        addUser(username, displayName, password)

    def currentUser(self):
        pass
