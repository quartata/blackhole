import sqlite3

with sqlite3.connect("db.sqlite3") as connection:
    db = connection.cursor()
    db.execute("create table blacklist (rev integer primary key autoincrement, keyword text, removal boolean);")
