import os.path
import pickle
import requests


class Blacklist:
    def __init__(self, rev, blacklist):
        self.rev = rev
        self.blacklist = blacklist


if os.path.isfile("blacklist.p"):
    with open("blacklist.p", "rb") as pickle_file:
        blacklist = pickle.load(pickle_file)
else:
    blacklist = Blacklist(0, set())

data = requests.get("http://localhost/blackhole/cgi-bin/fetch.py", params={"rev": blacklist.rev}).json()
blacklist.rev = data["rev"]

blacklist.blacklist |= set(data["added"])
blacklist.blacklist -= set(data["removed"])

with open("blacklist.p", "wb") as save:
    pickle.dump(blacklist, save)
