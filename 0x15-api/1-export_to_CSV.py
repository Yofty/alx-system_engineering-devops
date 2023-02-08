#!/usr/bin/python3
"""
using https://jsonplaceholder.typicode.com
returns information about employee TODO list progress
extended to export data in the CSV format
"""
import re
import requests
import sys
import json


API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(API, id)).json()
            todos_res = requests.get('{}/todos'.format(API)).json()
            user_name = user_res.get('username')
            todos = list(filter(lambda x: x.get('userId') ==id, todos_res))
            with open('{}.csv'.format(id), 'w') as file:
                for todo in todos:
                    file.write(
                            '"{}", "{}", "{}", "{}"\n'.format(
                                id,
                                user_name,
                                todo.get('completed'),
                                todo.get('title')
                                )
                            )
