from flask import Flask             #facilitate flask webserving
from flask import session           #facilitate user sessions
from utils.db import initializeUsersTable, addUser, getUserByUsername
from werkzeug.security import generate_password_hash, check_password_hash

class AuthService:

    activeUsers = {}

    def __init__(self):
        initializeUsersTable()

    def currentUser(self):
        if "username" in session:
            userData = getUserByUsername(session.get("username"))
            return userData

        return None

    def login(self, username, password):
        userData = getUserByUsername(username)

        if userData and username == userData[1]:
            if check_password_hash(userData[3], password):
                session["username"] = username
                return True

        return False


    def register(self, username, displayName, password):
        hashedPw = generate_password_hash(password)
        addUser(username, displayName, hashedPw)
