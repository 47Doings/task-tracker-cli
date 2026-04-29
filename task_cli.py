import sys
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    tasks = load_tasks()

    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": str(datetime.now()),
        "updatedAt": str(datetime.now())
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print(f"Task added successfully (ID: {new_task['id']})")


def main():
    args = sys.argv

    if len(args) < 2:
        print("Usage: python task_cli.py <command>")
        return

    command = args[1]

    if command == "add":
        if len(args) < 3:
            print("Please provide a task description")
            return

        description = args[2]
        add_task(description)

    else:
        print("Unknown command:", command)


if __name__ == "__main__":
    main()