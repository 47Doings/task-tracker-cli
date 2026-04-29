# Task Tracker CLI

A simple command-line app to manage tasks using Python and JSON file storage.

---

## Features

* Add tasks
* View all tasks
* Update tasks
* Delete tasks
* Mark tasks as in-progress or done

---

## How to Run

```bash
python task_cli.py <command>
```

---

## Commands

```bash
add "task description"
list
update <id> "new description"
delete <id>
mark-in-progress <id>
mark-done <id>
```

---

## Example

```bash
python task_cli.py add "Learn Python"
python task_cli.py list
python task_cli.py mark-done 1
```

---

## Data Storage

Tasks are stored locally in a `tasks.json` file.

---

## Author

Built as a learning project using Python.

## Project URL

https://github.com/47Doings/task-tracker-cli

https://roadmap.sh/projects/task-tracker