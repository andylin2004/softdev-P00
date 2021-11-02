# Team Name: Sleepy Programmers: Andy Lin, Shadman Rakib, Raymond Yeung
# SoftDev
# K15 -- User sessions on website via Flask
# 2021-10-18

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session           #facilitate user sessions
from flask import redirect
from os import urandom

from utils.db import initializeDatabase;
from utils.auth import AuthService;

app = Flask(__name__)    #create Flask object

auth = AuthService()

@app.route("/")
def disp_loginpage():
    currentUser = auth.currentUser()
    print("currentUser:", currentUser)

    if currentUser:
        return render_template('homePage.html', username=currentUser[2])
    return render_template( 'login.html' ) # Render the login template


@app.route("/login", methods=['GET', 'POST'])
def authenticate():
    # The requests property contains the values property. The value property contains
    # data from both requests.args and requests.form.

    if request.method == "GET": #for when you refresh the website
        return disp_loginpage()
    else: #when you log in from /
        username = request.values['username']
        password = request.values['password']

        if auth.login(username, password):
            return render_template('homePage.html', username=username)
        else:
            return render_template('login.html', error='Incorrect username or password')

@app.route("/logout")
def logout():
    if session.get("username"):
        session.pop("username")
    return redirect("/")

if __name__ == "__main__": #false if this file imported as module
    initializeDatabase()
    app.secret_key = urandom(32) # randomized secret key
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
