from flask import Flask
from flask import render_template
app = Flask(__name__)

from utils.database import initializeDatabase;

@app.route("/")
def index():
    return render_template( 'homePage.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/editBlog")
def editBlog():
    return render_template('editBlog.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    return "filler"

if __name__ == "__main__":  # true if this file NOT imported
    initializeDatabase()
    app.debug = True        # enable auto-reload upon code change
    app.run()
