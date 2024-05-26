#!/usr/bin/python3
"""
export data got from a request using an API in json format format
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    username = requests.get(url+"users/{}".format(argv[1])).json().get(
            "username"
            )
    todos = requests.get(url+"todos", params={"userId": argv[1]}).json()
    t_arr = []
    for todo in todos:
        task = todo.get("title")
        completed = todo.get("completed")
        t_arr.append({
            "task": task,
            "completed": completed,
            "username": username}
            )
        obj = {argv[1]: t_arr}
    filename = argv[1]+".json"
    with open(filename, "w") as file:
        json_obj = json.dumps(obj)
        file.write(json_obj)
