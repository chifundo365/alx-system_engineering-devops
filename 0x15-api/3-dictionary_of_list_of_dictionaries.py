#!/usr/bin/python3
"""
export data got from a request using an API in json format format
Gets all the tasks of all the employees
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    todos = requests.get(url+"todos").json()
    obj = {}
    id = None
    for todo in todos:
        username = requests.get(url+"/users/{}".format(todo.get("userId")))
        username = username.json().get("username")
        user_id = todo.get("userId")
        task = todo.get("title")
        completed = todo.get("completed")
        todo_obj = {
            "username": username,
            "task": task,
            "completed": completed
            }

        if not id or id != todo.get("userId"):
            obj.update({user_id: [todo_obj]})
        else:
            obj.get(user_id).append(todo_obj)
        id = user_id

    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json_obj = json.dumps(obj)
        file.write(json_obj)
