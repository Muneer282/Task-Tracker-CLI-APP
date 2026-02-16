import argparse
import json
from datetime import datetime

# Create parser
parser = argparse.ArgumentParser(prog="task-cli")

# Create subcommands (add / update / in progress / delete)
subparsers = parser.add_subparsers(dest="command")

# ===== add =====
add_parser = subparsers.add_parser("add")
add_parser.add_argument("name")

# ===== update =====
update_parser = subparsers.add_parser("update")
update_parser.add_argument("id", type=int)
update_parser.add_argument("name")

# ===== in progress =====
in_progress_parser = subparsers.add_parser("mark-in-progress")
in_progress_parser.add_argument("id", type=int)

# ===== done =====
done_parser = subparsers.add_parser("mark-done")
done_parser.add_argument("id", type=int)

# ===== list =====
list_parser = subparsers.add_parser("list")

# ===== list done =====
list_done_parser = subparsers.add_parser("list-done")

# ===== list todo =====
list_todo_parser = subparsers.add_parser("list-todo")

# ===== list in-progress =====
list_in_progress_parser = subparsers.add_parser("list-in-progress")

# ===== delete =====
delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("id", type=int)

# Read commands
args = parser.parse_args()

# Execute commands
if args.command == "add":
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    tasks.append(
        {
            "id": len(tasks) + 1,
            "description": args.name,
            "status": "todo",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
    )
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)
    print(f"Task added successfully: {args.name}")

elif args.command == "update":
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    tasks[args.id - 1]["description"] = args.name
    tasks[args.id - 1]["updated_at"] = datetime.now().isoformat()
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)
    print(f"Task updated successfully with id {args.id} to {args.name}")

elif args.command == "mark-in-progress":
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    tasks[args.id - 1]["status"] = "in-progress"
    tasks[args.id - 1]["updated_at"] = datetime.now().isoformat()
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)
    print(f"Task marked as in progress with id {args.id} successfully")

elif args.command == "mark-done":
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    tasks[args.id - 1]["status"] = "done"
    tasks[args.id - 1]["updated_at"] = datetime.now().isoformat()
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)
    print(f"Task marked as done with id {args.id} successfully")

elif args.command == "list":
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    for task in tasks:
        print(f"{task['id']} - {task['description']} - {task['status']}")
    print("Listed all tasks successfully")

elif args.command == "list-done":
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    for task in tasks:
        if task["status"] == "done":
            print(f"{task['id']} - {task['description']} - {task['status']}")
    print("Listed all done tasks successfully")

elif args.command == "list-todo":
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    for task in tasks:
        if task["status"] == "todo":
            print(f"{task['id']} - {task['description']} - {task['status']}")
    print("Listed all todo tasks successfully")

elif args.command == "list-in-progress":
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    for task in tasks:
        if task["status"] == "in-progress":
            print(f"{task['id']} - {task['description']} - {task['status']}")
    print("Listed all in progress tasks successfully")

elif args.command == "delete":
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    tasks.pop(args.id - 1)
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)
    print(f"Deleted task with id {args.id} successfully")
    
else:
    print("Invalid command")
