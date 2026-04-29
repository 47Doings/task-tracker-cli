import sys
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


# ----------------- LOAD / SAVE -----------------

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# ----------------- ADD TASK -----------------

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


# ----------------- LIST TASKS -----------------

def list_tasks():
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"""
ID: {task['id']}
Description: {task['description']}
Status: {task['status']}
CreatedAt: {task['createdAt']}
UpdatedAt: {task['updatedAt']}
------------------------
""")


# ----------------- DELETE TASK -----------------

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = []

    found = False

    for task in tasks:
        if task["id"] == task_id:
            found = True
        else:
            updated_tasks.append(task)

    if not found:
        print(f"Task with ID {task_id} not found.")
        return

    save_tasks(updated_tasks)
    print(f"Task {task_id} deleted successfully.")


# ----------------- UPDATE TASK -----------------

def update_task(task_id, new_description):
    tasks = load_tasks()

    found = False

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = str(datetime.now())
            found = True
            break

    if not found:
        print(f"Task with ID {task_id} not found.")
        return

    save_tasks(tasks)
    print(f"Task {task_id} updated successfully.")

def mark_status(task_id, status):
    tasks = load_tasks()

    found = False

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = str(datetime.now())
            found = True
            break

    if not found:
        print(f"Task with ID {task_id} not found.")
        return

    save_tasks(tasks)
    print(f"Task {task_id} marked as {status}.")
# ----------------- MAIN CLI -----------------

def main():
    args = sys.argv

    if len(args) < 2:
        print("Usage: python task_cli.py <command>")
        return

    command = args[1]

    # ADD
    if command == "add":
        if len(args) < 3:
            print("Please provide a task description")
            return

        description = args[2]
        add_task(description)

    # LIST
    elif command == "list":
        list_tasks()

    # DELETE
    elif command == "delete":
        if len(args) < 3:
            print("Please provide task ID")
            return

        task_id = int(args[2])
        delete_task(task_id)

    # UPDATE
    elif command == "update":
        if len(args) < 4:
            print("Usage: python task_cli.py update <id> <new description>")
            return

        task_id = int(args[2])
        new_description = args[3]
        update_task(task_id, new_description)

    # MARK IN PROGRESS
    elif command == "mark-in-progress":
        if len(args) < 3:
            print("Please provide task ID")
            return

        task_id = int(args[2])
        mark_status(task_id, "in-progress")

    # MARK DONE
    elif command == "mark-done":
        if len(args) < 3:
            print("Please provide task ID")
            return

        task_id = int(args[2])
        mark_status(task_id, "done")

    else:
        print("Unknown command:", command)


if __name__ == "__main__":
    main()