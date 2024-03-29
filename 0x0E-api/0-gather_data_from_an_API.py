#!/usr/bin/python3
"""API Practice"""
import requests
import sys


def main():
    """Gather data from an API"""
    employee_ID = int(sys.argv[1])
    URL = 'https://jsonplaceholder.typicode.com'
    reply = requests.get("{}/users".format(URL))\
        .json()
    for item in reply:
        if item['id'] == employee_ID:
            employee_json = item

    employee_name = employee_json.get('name')
    task_json = requests.get("{}/todos".format(URL)).json()

    task_list = [x for x in task_json if x['userId'] == employee_ID]
    tasks_done = [x for x in task_list if x['completed']]
    tasks_total = len(task_list)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(tasks_done), tasks_total))
    for task in task_list:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    main()
