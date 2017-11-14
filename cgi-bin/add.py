#!/usr/bin/python3

import cgi
import sqlite3

params = cgi.FieldStorage()

if "keyword" not in params or "type" not in params:
    print("Status: 400 Bad Request\n")
else:
    keyword = params.getvalue("keyword")
    blacklist = params.getvalue("type")

    with sqlite3.connect("../db.sqlite3") as db:
        db.execute("insert into blacklist (keyword, type, removal) values (?, ?, 0);", (keyword, blacklist))
        db.commit()

        print("Content-Type: text/plain\n")
        print("success")