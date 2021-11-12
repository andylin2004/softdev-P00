from flask import Flask             #facilitate flask webserving
from flask import session           #facilitate user sessions
from os import urandom
from utils.db import initializeUsersTable, addUser, getUserByUsername
from werkzeug.security import generate_password_hash, check_password_hash
from utils.response import Response

class AuthService:

    activeUsers = {} # Used to map sessionIDs to usernames

    def __init__(self):
        '''Runs when an object is initialized'''

        initializeUsersTable() # Create users table if it doesn't exist

    def currentUser(self):
        '''Gets the data on the user that is currently signed in. 
        If no one is signed in, the function returns None.'''

        try:
            if "sessionID" in session:
                sessionID = session.get("sessionID")
                username = self.activeUsers[sessionID]

                userDataResponse = getUserByUsername(username)

                if (userDataResponse.success):
                    userData = userDataResponse.data
                    return Response(True, userData, "")
                else:
                    Response(True, None, "")
            return Response(False, None, "")
        except Exception as err:
            return Response(False, None, err)

    def login(self, username, password):
        '''Logs a user in and gives them a session id that is stored on client
        and server (in activeUsers)'''

        try:
            userDataResponse = getUserByUsername(username)

            if (userDataResponse.success):
                userData = userDataResponse.data
                if userData and username == userData["username"]:
                    if check_password_hash(userData["password"], password):
                        sessionID = urandom(32)
                        session["sessionID"] = sessionID
                        self.activeUsers[sessionID] = username

                        return Response(True, None, "")

            return Response(False, None, "")
        except Exception as err:
            return Response(False, None, err)

    def register(self, username, displayName, password):
        '''Registers a user and adds there information to the database'''

        try:
            hashedPw = generate_password_hash(password) # Create a hash from the password
            
            #Store the hash, not original password
            addUserResponse = addUser(username, displayName, hashedPw) # Store the user in the database

            if addUserResponse.success:
                return Response(True, None, "")
            else:
                return Response(False, None, addUserResponse.errorMessage)

        except Exception as err:
            return Response(False, None, err)

    def logout(self):
        '''Logs the user out'''

        try:
            if session.get("sessionID"): # Check is there is a sessionID in request session object
                if session.get("sessionID") in self.activeUsers: # Check is there is a sessionID in server's activeUsers dictionary
                    self.activeUsers.pop(session.get("sessionID")) # Remove the sessionID on the server
                    
                session.pop("sessionID") # Remove the sessionID on the client

            return Response(True, None, "")
            
        except Exception as err:
            return Response(False, None, err)
