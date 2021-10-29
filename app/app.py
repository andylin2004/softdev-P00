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

app = Flask(__name__)    #create Flask object

@app.route("/")
def disp_loginpage():
    if "username" in session:
        return render_template('response.html', username=session["username"])
    return render_template( 'login.html' ) # Render the login template


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    # The requests property contains the values property. The value property contains
    # data from both requests.args and requests.form.
    
    if request.method == "GET": #for when you refresh the website
        return disp_loginpage()
    else: #when you log in from /
        username = request.values['username']
        password = request.values['password']

        if username == "dn":
            if password == "1738":
                session["username"] = username
                #response to a person who has the right credentials and logs in
                return render_template('response.html', username=username)
            else:
                return render_template('login.html', error='password') #wrong pw
        else:
            return render_template('login.html', error='username') #wrong user

@app.route("/logout")
def logout():
    if session.get("username"):
        session.pop("username")
    return redirect("/")

if __name__ == "__main__": #false if this file imported as module
    app.secret_key = urandom(32) # randomized secret key
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
