#!/usr/bin/python3
''' Export to CSV '''

import csv
import json
import sys
import urllib.request as req


def export_csv(id):
    URI1 = f"https://jsonplaceholder.typicode.com/todos/"
    URI2 = f"https://jsonplaceholder.typicode.com/users/{id}"

    usr_name = ""
    with req.urlopen(URI2) as resp:
        to_print = resp.read().decode("UTF-8")
        data = json.loads(to_print)
        usr_name = data["name"]
    with req.urlopen(URI1) as resp:
        to_print = resp.read().decode("UTF-8")
        data = json.loads(to_print)
    with open(f"{id}.csv", 'w+', newline='') as csvfile:
        to_write = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
        for ds in data:
            if ds["userId"] == int(id):
                to_write.writerow([id, usr_name, ds["completed"], ds["title"]])


if __name__ == "__main__":
    user_id = sys.argv[1]
    export_csv(user_id)
