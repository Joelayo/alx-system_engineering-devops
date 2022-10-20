#!/usr/bin/python3
'''A script that gathers data from an API and exports it to a JSON file.
'''
import json
import requests


API_URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''


if __name__ == '__main__':
    users = requests.get(API_URL + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(API_URL + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
