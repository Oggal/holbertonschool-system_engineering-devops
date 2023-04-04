#!/usr/bin/python3
import requests
from sys import argv


def main():
    """Gather data from an API"""
    employee_ID = int(argv[1])
    URL = 'https://jsonplaceholder.typicode.com'
    employee_json = requests.get("{}/users".format(URL))\
        .json()[employee_ID - 1]

    print(employee_json)
    print(type(employee_json))
    employee_name = employee_json.get('name')
    task_json = requests.get("{}/todos".format(URL)).json()

    task_list = [x for x in task_json if x['userId'] == employee_ID]
    tasks_done = [x for x in task_list if x['completed']]
    tasks_total = len(task_list)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(tasks_done), tasks_total))
    for task in task_list:
        if not task.get('completed'):
            print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    main()
