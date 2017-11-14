#!/usr/bin/python3

import cgi
import json
import sqlite3

params = cgi.FieldStorage()

if "rev" not in params or "type" not in params:
    print("Status: 400 Bad Request\n")
else:
    rev = params.getvalue("rev")
    blacklist = params.getvalue("type")

    with sqlite3.connect("../db.sqlite3") as db:
        current_rev = db.execute("select rev from blacklist where type = ? order by rev desc limit 1;", (blacklist,))

        changes = db.execute("select keyword, removal from blacklist where rev > ? and type = ? order by rev asc",
                             (rev, blacklist))

        print("Content-Type: application/json\n")
        print(json.dumps({
            "rev": current_rev.fetchone()[0],
            "changes": changes.fetchall(),
        }))
