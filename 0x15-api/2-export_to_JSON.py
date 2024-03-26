#!/usr/bin/python3
''' Export to JSON '''

import json
import sys
import urllib.request as req


def export_csv(id):
    URI1 = f"https://jsonplaceholder.typicode.com/todos/"
    URI2 = f"https://jsonplaceholder.typicode.com/users/{id}"

    usr_name = ""
    user_data = {}
    value = []
    with req.urlopen(URI2) as resp:
        to_print = resp.read().decode("UTF-8")
        usr_data = json.loads(to_print)
        usr_name = usr_data["username"]
    with req.urlopen(URI1) as resp:
        to_print = resp.read().decode("UTF-8")
        todo_data = json.loads(to_print)
    for ds in todo_data:
        if ds["userId"] == int(id):
            vals = {
                "task": ds["title"],
                "completed": ds["completed"],
                "username": usr_name
            }
            value.append(vals)
    user_data[id] = value
    with open(f'{id}.json', "w") as data:
        json.dump(user_data, data)


if __name__ == "__main__":
    user_id = sys.argv[1]
    export_csv(user_id)
