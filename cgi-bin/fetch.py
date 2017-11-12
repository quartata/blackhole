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
        added = db.execute("select keyword from blacklist where rev > ? and removal = 0;", (rev,))
        removed = db.execute("select keyword from blacklist where rev > ? and removal = 1;", (rev,))

        print("Content-Type: application/json\n")
        print(json.dumps({
            "rev": current_rev.fetchone()[0],
            "added": [x[0] for x in added.fetchall()],
            "removed": [x[0] for x in removed.fetchall()]
        }))
