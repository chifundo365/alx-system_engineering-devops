#!/usr/bin/python3
"""
export data got from a request using an API in csv format
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    username = requests.get(url+"users/{}".format(argv[1])).json().get(
            "username"
            )
    tasks = requests.get(url+"todos", params={"userId": argv[1]}).json()
    data = []
    for task in tasks:
        data.append([argv[1],
                    username, task.get("completed"),
                    task.get('title')])
    filename = argv[1]+".csv"
    with open(filename, "w", newline="") as file:
        csvwriter = csv.writer(file, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(data)
