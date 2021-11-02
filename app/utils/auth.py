from flask import Flask             #facilitate flask webserving
from flask import session           #facilitate user sessions
from utils.db import initializeUsersTable, addUser, getUserByUsername;

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
            if password == userData[3]:
                session["username"] = username
                return True

        return False
        

    def register(self, username, displayName, password):
        addUser(username, displayName, password)
