# 📝 To-Do List Manager (Python CLI)

A simple **command-line to-do list application** built in Python. It allows users to add, view, and mark tasks as completed. All tasks are stored persistently in a local JSON file.

---

## 📁 File Structure

todo_list/
├── todo_list.py
└── todo_list.json # (auto-created)

yaml
Copy code

---

## 🚀 Features

- ✅ View tasks with status (pending/completed)
- ➕ Add new tasks
- ✔️ Mark tasks as complete
- 💾 Saves tasks in a JSON file for persistence
- 🧱 Minimal dependencies — uses only Python's standard library

---

## 🛠 Requirements

- Python 3.6+

No external packages are required.

---

## ▶️ How to Run

1. **Clone or download** the repository.

2. Open a terminal or command prompt and navigate to the directory containing `todo_list.py`.

3. Run the program using:

```bash
python todo_list.py
📦 JSON File Format
All tasks are saved in todo_list.json in this format:

json
Copy code
{
  "tasks": [
    {
      "description": "Buy groceries",
      "complete": false
    },
    {
      "description": "Call Alice",
      "complete": true
    }
  ]
}
📋 Menu Options
When the program runs, you'll see:

pgsql
Copy code
To-Do List Manager
1. View tasks
2. Add task
3. Complete task
4. Exit
Option 1: Shows all tasks with their status.

Option 2: Lets you enter a new task description.

Option 3: Prompts for a task number to mark as complete.

Option 4: Exits the application.

💡 Future Improvements (Ideas)
🗑 Delete tasks

🗓 Add due dates

⏫ Task priorities

🌐 Web interface (Flask or Django)

📱 Mobile version (Kivy)

📄 License
This project is open source and free to use.

