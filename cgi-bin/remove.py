#!/usr/bin/python3

import cgi
import cgitb
import sqlite3

cgitb.enable()

params = cgi.FieldStorage()

if "keyword" not in params:
    print("Content-Type: text/plain\n")
else:
    with sqlite3.connect("../db.sqlite3") as connection:
        db = connection.cursor()

        db.execute("insert into blacklist (keyword, removal) values (?, 1);", (params.getvalue("keyword"),))
        connection.commit()

        print("Content-Type: text/plain\n")
        print("success")
