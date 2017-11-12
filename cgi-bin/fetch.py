#!/usr/bin/python3

import cgi
import cgitb
import json
import sqlite3

cgitb.enable()

params = cgi.FieldStorage()

if "rev" not in params:
    print("Content-Type: text/plain\n")
else:
    rev = params.getvalue("rev")

    with sqlite3.connect("../db.sqlite3") as db:
        current_rev = db.execute("select rev from blacklist order by rev desc limit 1;")
        changes = db.execute("select keyword, removal from blacklist where rev > ?", (rev,))

        print("Content-Type: application/json\n")
        print(json.dumps({
            "rev": current_rev.fetchone()[0],
            "changes": changes.fetchall(),
        }))
