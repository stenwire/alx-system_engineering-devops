#!/usr/bin/python3
"""A Python script that, using a REST API,
for a given employee ID,returns information about
his/her todo list progress
"""
import requests
from sys import argv


if __name__ == '__main__':
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

    # Get total no of done todo
    todo_len = len(u_todo)

    # Save content to csv file
    with open(f'{USER_ID}.csv', 'w') as f:
        for todo in range(todo_len):
            TASK_TITLE = u_todo[todo]['title']
            TASK_COMPLETED_STATUS = u_todo[todo]['completed']
            TASK_TITLE = u_todo[todo]['title']
            str_1 = f'"{USER_ID}","{USERNAME}",'
            str_2 = f'"{TASK_COMPLETED_STATUS}","{TASK_TITLE}"'
            line = str_1 + str_2
            f.write(line)
            f.write('\n')
