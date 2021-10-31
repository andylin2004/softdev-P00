import sqlite3

db = sqlite3.connect("database.db")
c = db.cursor()

def search(searchQuery):
    c.execute("SELECT * FROM blogs WHERE blogTitle LIKE '%:title%'", {'title': searchQuery})
    data = c.fetchall()