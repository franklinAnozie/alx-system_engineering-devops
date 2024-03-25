#!/usr/bin/env python3

import json
import urllib.request as req

URI = "https://jsonplaceholder.typicode.com/users"
resp = req.urlopen(URI)
print_ = resp.read()
printing = print_.decode("UTF-8")
check = json.loads(printing)

for mem in check:
    print(mem)
