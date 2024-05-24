#!/usr/bin/python3
"""
Prints information about a user's TODO list progrees given employee id
"""
import requests
from sys import argv

user_id = argv[1]
todos_url = "https://jsonplaceholder.typicode.com/todos"
user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)


user_name = requests.get(user_url).json().get('name')
res = requests.get(todos_url, params={'userId': user_id})
total_tasks = 0
tasks_done = []

# Getting number of tasks completed and total tasks
for todos in res.json():
    if todos.get('completed', None):
        tasks_done.append(todos.get('title'))
    total_tasks += 1

msg = "Employee {} is done with tasks({}/{}):".format(
        user_name,
        len(tasks_done),
        total_tasks
        )

print(msg)

# Printing titles of the completed tasks
for t in tasks_done:
    print("\t  {}".format(t))
