# 🧠 Task Management System
The Task Management System is a simple and intuitive command-line interface (CLI) for managing tasks. It provides a set of commands to add, update, mark as in-progress, mark as done, list, and delete tasks. The CLI interacts with a JSON file to store and retrieve task data, making it easy to use and persistent.


## 🚀 Features
- Add new tasks with a given name
- Update the name of a task with a given ID
- Mark a task with a given ID as in-progress
- Mark a task with a given ID as done
- List all tasks or tasks with a specific status (todo, in-progress, done)
- Delete a task with a given ID
- Store task data in a JSON file for persistence


## 🛠️ Tech Stack
* `argparse` for parsing CLI commands
* `json` for interacting with the `tasks.json` file
* `datetime` for generating timestamps


## 📦 Installation
To install the Task Management System, follow these steps:
1. Clone the repository using `git clone`
2. Navigate to the project directory using `cd`
3. Install the required dependencies using `pip install -r requirements.txt`


## 💻 Usage
To use the Task Management System, follow these steps:
1. Run the CLI using `python task_cli.py`
2. Use the available commands to manage tasks:
	* `add`: Add a new task with a given name
	* `update`: Update the name of a task with a given ID
	* `mark-in-progress`: Mark a task with a given ID as in-progress
	* `mark-done`: Mark a task with a given ID as done
	* `list`, `list-done`, `list-todo`, `list-in-progress`: List all tasks or tasks with a specific status
	* `delete`: Delete a task with a given ID


## Notes

### JSONDecodeError when running the CLI for the first time

When running the command for the first time, you may encounter the following error:

```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

#### Cause

This happens because the application tries to read data from a JSON file that is either:

* Empty
* Not yet initialized
* Contains invalid JSON content

The `json.load()` function expects valid JSON data, and an empty file is not considered valid JSON.

#### Solution

Make sure the data file (e.g. `tasks.json`) contains valid JSON.
Initialize it with an empty list:

```json
[]
```

#### Recommended Improvement

The application should automatically create and initialize the data file if it does not exist. Example:

```python
import json
import os

if not os.path.exists("tasks.json"):
    with open("tasks.json", "w") as f:
        json.dump([], f)

with open("tasks.json", "r") as f:
    tasks = json.load(f)
```

This ensures the CLI works correctly on the first run without manual setup.

---

## 📂 Project Structure
```markdown
.
├── task_cli.py
├── tasks.json
├── requirements.txt
└── README.md
```


### Running the CLI Command on Windows

If the command `task-cli` is not recognized, run it using:

```
.\task-cli add "Task name"
```

Windows does not execute commands from the current directory unless prefixed with `.\` or added to the system `PATH`.

## 🤝 Contributing
To contribute to the Task Management System, please follow these steps:
1. Fork the repository using `git fork`
2. Create a new branch using `git branch`
3. Make changes and commit them using `git commit`
4. Push the changes using `git push`
5. Create a pull request using `git pull-request`

## 📝 License
The Task Management System is licensed under the MIT License.

## 📬 Contact
For any questions or concerns, please contact us at [support@example.com](mailto:support@example.com).

## 💖 Thanks Message
We hope you find the Task Management System useful! If you have any feedback or suggestions, please don't hesitate to reach out.

### Project URL
https://roadmap.sh/projects/task-tracker
