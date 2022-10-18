#!/usr/bin/python3
"""A Python script that, using a REST API,
for a given employee ID,returns information about
his/her todo list progress
"""
import requests
import json
from sys import argv


def main():
    """Query https://jsonplaceholder.typicode.com for info"""
    # Get user ID from STDIN
    args = argv
    u_id = args[1]

    # Making a GET request
    req_1 = requests.get(
        'https://jsonplaceholder.typicode.com/users/{0}/todos'
        .format(u_id))
    req_2 = requests.get(
        'https://jsonplaceholder.typicode.com/users/{0}'
        .format(u_id))

    # Extract data
    u_todo = req_1.json()
    u_info = req_2.json()
    USER_ID = u_info['id']
    USERNAME = u_info['username']
    todo_len = len(u_todo)

    data = {}
    data[USER_ID] = []

    with open(f'{USER_ID}.json', 'w') as f:
        for todo in range(todo_len):
            TASK_TITLE = u_todo[todo]['title']
            TASK_COMPLETED_STATUS = u_todo[todo]['completed']
            TASK_TITLE = u_todo[todo]['title']
            data[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })
        json.dump(data, f)


if __name__ == '__main__':
    main()
