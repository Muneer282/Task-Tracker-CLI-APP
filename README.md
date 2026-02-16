# Task-Tracker-CLI-APP
Build a CLI app to track your tasks and manage your to-do list.

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

### Running the CLI Command on Windows

If the command `task-cli` is not recognized, run it using:

```
.\task-cli add "Task name"
```

Windows does not execute commands from the current directory unless prefixed with `.\` or added to the system `PATH`.

### Project URL
https://github.com/Muneer282/Task-Tracker-CLI-APP.git
