#!/usr/bin/python3
"""A Python script that, using a REST API,
for a given employee ID,returns information about
his/her todo list progress
"""
import requests
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
    req_3 = requests.get(
        'https://jsonplaceholder.typicode.com/users/{0}/todos?completed=true'
        .format(u_id))

    # Extract data in json format
    u_todo = req_1.json()
    u_info = req_2.json()
    done_task = req_3.json()

    # Get total no of todo
    count = 0
    for todo in u_todo:
        count += 1
    todo_len = count

    # Get total no of done todo
    done_todo = len(done_task)

    # print(done_task[0]['title'])
    # Output info
    print(
        'Employee {0} is done with tasks ({1}/{2}):'
        .format(u_info['name'], done_todo, todo_len))

    for todo in range(len(done_task)):
        print('\t{0}'.format(done_task[todo]['title']))


if __name__ == '__main__':
    main()
