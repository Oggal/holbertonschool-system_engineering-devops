#!/usr/bin/python3
"""API Practice"""
import requests
import sys


def main():
    """Gather data from an API"""
    ID = int(sys.argv[1])
    datablock = build_data(ID)
    export_CSV(ID, datablock)


def get_employee(ID: int) -> dict:
    """Get employee"""
    URL = 'https://jsonplaceholder.typicode.com/users'
    reply = requests.get(URL).json()
    for item in reply:
        if item['id'] == ID:
            return item
    print("Employee not found")
    return {}


def get_todos(ID: int) -> list:
    """Get todos"""
    URL = 'https://jsonplaceholder.typicode.com/todos'
    reply = requests.get(URL).json()
    return [x for x in reply if x['userId'] == ID]


def build_data(ID: int) -> list:
    """Format data as desired"""
    name = get_employee(ID).get('username')
    tasks = get_todos(ID)
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


if __name__ == "__main__":
    main()
