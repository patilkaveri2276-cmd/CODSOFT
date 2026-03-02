import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import date

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

# Add task
def add_task():
    task_text = task_entry.get().strip()
    if task_text == "":
        messagebox.showwarning("Warning", "Enter a task!")
        return
    
    tasks.append({"text": task_text, "completed": False})
    save_tasks()
    display_tasks()
    task_entry.delete(0, tk.END)

# Delete completed tasks
def delete_completed():
    global tasks
    tasks = [task for task in tasks if not task["completed"]]
    save_tasks()
    display_tasks()

# Toggle complete
def toggle_task(index):
    tasks[index]["completed"] = not tasks[index]["completed"]
    save_tasks()
    display_tasks()

# Display tasks
def display_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for index, task in enumerate(tasks):
        var = tk.BooleanVar(value=task["completed"])

        # Add ✓ if completed
        display_text = task["text"]
        if task["completed"]:
            display_text = "✓ " + display_text

        cb = tk.Checkbutton(
            task_frame,
            text=display_text,
            variable=var,
            command=lambda i=index: toggle_task(i),
            font=("Arial", 11)
        )
        cb.pack(anchor="w", pady=3)

# Main Window
root = tk.Tk()
root.title("To-Do List - Internship Project")
root.geometry("400x500")

# Date
today_label = tk.Label(root, text="Today: " + str(date.today()),
                       font=("Arial", 12))
today_label.pack(pady=10)

# Entry
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Single Delete Button
delete_button = tk.Button(root, text="Delete Completed Tasks",
                          command=delete_completed,
                          bg="red", fg="white")
delete_button.pack(pady=5)

# Task Frame
task_frame = tk.Frame(root)
task_frame.pack(pady=20)

tasks = load_tasks()
display_tasks()

root.mainloop()
