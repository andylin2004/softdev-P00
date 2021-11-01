from flask import Flask
app = Flask(__name__)

from utils.database import initializeDatabase;

@app.route("/")
def index():
    return "Hey!"

if __name__ == "__main__":  # true if this file NOT imported
    initializeDatabase()
    app.debug = True        # enable auto-reload upon code change
    app.run()
