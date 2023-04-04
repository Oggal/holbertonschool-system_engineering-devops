#!/usr/bin/python3
"""API Practice"""
import json
import requests
import sys


def main():
    """Gather data from an API"""
    ID = int(sys.argv[1])
    datablock = fetch_json_data(ID)
    export_json(ID, datablock)


def fetch_employee(ID: int) -> dict:
    """Get employee"""
    URL = 'https://jsonplaceholder.typicode.com/users'
    reply = requests.get(URL).json()
    return find_employee(reply, ID)


def find_employee(datapack, ID: int):
    for item in datapack:
        if item['id'] == ID:
            return item
    print("Employee not found")
    return{}


def fetch_todos(ID: int) -> list:
    """Get todos"""
    URL = 'https://jsonplaceholder.typicode.com/todos'
    reply = requests.get(URL).json()
    return find_todos(reply, ID)


def find_todos(task_data, ID: int):
    return [x for x in task_data if x['userId'] == ID]


def fetch_json_data(ID: int) -> list:
    """Format data for JSON"""
    tasks = fetch_todos(ID)
    users = fetch_employee(ID)
    build_json_data(ID, tasks, users)


def build_json_data(ID: int, task_data, employee_data):
    """Get employee json data from fetched data """
    data = []
    for task in task_data:
        done = task['completed']
        name = employee_data['username']
        data.append(
            {'username': name, 'task': task['title'], 'completed': done})
    return data


def build_data(ID: int) -> list:
    """Format data as desired"""
    name = fetch_employee(ID).get('username')
    tasks = fetch_todos(ID)
    data = []
    for task in tasks:
        data.append('"{0}","{1}","{2}","{3}"'.format(
            ID, name, task.get('completed'), task.get('title')))
    return data


def export_CSV(ID: int, data: list):
    """export to CSV file"""
    filename = "{}.csv".format(ID)
    with open(filename, 'w') as f:
        for item in data:
            f.write(item + '\n')


def export_json(ID: int, data: dict):
    """export to json file"""
    filename = "{}.json".format(ID)
    datablock = {ID: data}
    with open(filename, 'w') as f:
        f.write(json.dumps(datablock))


def export_all_tasks():
    """Export all Tasks to Json"""
    URL = "https://jsonplaceholder.typicode.com/users"
    employee_data = requests.get(URL).json()
    URL = "https://jsonplaceholder.typicode.com/todos"
    task_data = requests.get(URL).json()
    data = {}
    for employee in employee_data:
        ID = employee.get('id')
        todos = find_todos(task_data, ID)
        data[ID] = build_json_data(ID, todos, employee)
    # Write Data to file
    with open("todo_all_employees.json", 'w') as f:
        f.write(json.dumps(data))


if __name__ == "__main__":
    export_all_tasks()
