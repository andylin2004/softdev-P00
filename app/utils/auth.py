from flask import Flask             #facilitate flask webserving
from flask import session           #facilitate user sessions
from os import urandom
from utils.db import initializeUsersTable, addUser, getUserByUsername
from werkzeug.security import generate_password_hash, check_password_hash
from utils.response import Response

class AuthService:

    activeUsers = {}

    def __init__(self):
        initializeUsersTable()

    def currentUser(self):
        if "sessionID" in session:
            sessionID = session.get("sessionID")
            username = self.activeUsers[sessionID]

            userDataResponse = getUserByUsername(username)

            if (userDataResponse.success):
                userData = userDataResponse.payload
                return Response(True, userData, "")
            else:
                Response(True, None, "")
        return Response(False, None, "")

    def login(self, username, password):
        userDataResponse = getUserByUsername(username)

        if (userDataResponse.success):
            userData = userDataResponse.payload
            if userData and username == userData["username"]:
                if check_password_hash(userData["password"], password):
                    sessionID = urandom(32)
                    session["sessionID"] = sessionID
                    self.activeUsers[sessionID] = username

                    return Response(True, True, "")

        return Response(False, False, "")

    def register(self, username, displayName, password):
        hashedPw = generate_password_hash(password)
        addUserResponse =  addUser(username, displayName, hashedPw)

        return Response(addUserResponse.success, addUserResponse.success, "")

    def logout(self):
        if session.get("sessionID"):
            if session.get("sessionID") in self.activeUsers:
                self.activeUsers.pop(session.get("sessionID"))

            session.pop("sessionID")
        return Response(True, True, "")
