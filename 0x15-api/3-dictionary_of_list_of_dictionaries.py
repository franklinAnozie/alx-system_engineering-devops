#!/usr/bin/python3
''' Export to JSON '''

import json
import urllib.request as req


def export_csv():
    URI1 = f"https://jsonplaceholder.typicode.com/todos/"
    URI2 = f"https://jsonplaceholder.typicode.com/users/"

    users = {}
    todos = {}
    with req.urlopen(URI2) as resp:
        to_print = resp.read().decode("UTF-8")
        data = json.loads(to_print)
        for d in data:
            users[d["id"]] = d["username"]
    with req.urlopen(URI1) as resp:
        to_print = resp.read().decode("UTF-8")
        data = json.loads(to_print)
        for d in data:
            if d["userId"] not in todos:
                todos[d["userId"]] = [
                    {
                        "username": users[d["userId"]],
                        "task": d["title"],
                        "completed": d["completed"]
                    }
                ]
            else:
                todos[d["userId"]].append(
                    {
                        "username": users[d["userId"]],
                        "task": d["title"],
                        "completed": d["completed"]
                    }
                )
    with open("todo_all_employees.json", "w") as data:
        json.dump(todos, data)


if __name__ == "__main__":
    export_csv()
