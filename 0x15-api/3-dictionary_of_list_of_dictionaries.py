#!/usr/bin/python3
"""A Python script that, using a REST API,
for a given employee ID,returns information about
his/her todo list progress
"""
import requests
import json


def main():
    """Query https://jsonplaceholder.typicode.com for info"""
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    userdict = {}
    usernamedict = {}
    for user in users:
        uid = user.get("id")
        userdict[uid] = []
        usernamedict[uid] = user.get("username")
    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    for task in todo:
        taskdict = {}
        uid = task.get("userId")
        taskdict["task"] = task.get('title')
        taskdict["completed"] = task.get('completed')
        taskdict["username"] = usernamedict.get(uid)
        userdict.get(uid).append(taskdict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(userdict, jsonfile)


if __name__ == '__main__':
    main()
