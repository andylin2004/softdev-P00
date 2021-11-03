from flask import Flask             #facilitate flask webserving
from flask import session           #facilitate user sessions
from utils.db import initializeUsersTable, addUser, getUserByUsername
from werkzeug.security import generate_password_hash, check_password_hash
from os import urandom

class AuthService:

    activeUsers = {}

    def __init__(self):
        initializeUsersTable()

    def currentUser(self):
        if "sessionID" in session:
            sessionID = session.get("sessionID")
            username = se;f.activeUsers[sessionID]

            userData = getUserByUsername(username)
            return userData

        return None

    def login(self, username, password):
        userData = getUserByUsername(username)

        if userData and username == userData[1]:
            if check_password_hash(userData[3], password):
                sessionID = urandom(32)
                session["sessionID"] = sessionID
                self.activeUsers[sessionID] = username

                return True

        return False

    def register(self, username, displayName, password):
        hashedPw = generate_password_hash(password)
        addUser(username, displayName, hashedPw)
