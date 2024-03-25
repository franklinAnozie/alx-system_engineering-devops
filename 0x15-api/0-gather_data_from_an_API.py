#!/usr/bin/python3
''' Gather data from an API using urllib '''

import json
import sys
import urllib.request as req


def api_req(id):
    URI1 = f"https://jsonplaceholder.typicode.com/todos/"
    URI2 = f"https://jsonplaceholder.typicode.com/users/{id}"

    user_name = ""
    user_data = []
    num_of_done = 0
    with req.urlopen(URI2) as resp:
        to_print = resp.read().decode("UTF-8")
        data = json.loads(to_print)
        user_name = data["name"]
    with req.urlopen(URI1) as resp:
        to_print = resp.read().decode("UTF-8")
        data = json.loads(to_print)
        for ds in data:
            if ds["userId"] == int(id):
                user_data.append(ds)
                if ds["completed"]:
                    num_of_done += 1
        num_of_tasks = len(user_data)
    
    print(f"Employee {user_name} is done with tasks({num_of_done}/{num_of_tasks}):")

    for mem in user_data:
        if mem["completed"]:
            print (f'\t {mem["title"]}')


if __name__ == '__main__':
    user_input = sys.argv[1]
    api_req(user_input)
