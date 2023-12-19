#To do list 
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        # Create and set up the main menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.main_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Main Menu", menu=self.main_menu)

        self.main_menu.add_command(label="Show Tasks", command=self.show_tasks)
        self.main_menu.add_command(label="Add Task", command=self.add_task)
        self.main_menu.add_command(label="Mark Task as Completed", command=self.mark_task)
        self.main_menu.add_separator()
        self.main_menu.add_command(label="Exit", command=self.root.destroy)

        # Create the table for displaying tasks
        self.table = ttk.Treeview(self.root, columns=("Description", "Status"), show="headings", selectmode="browse")
        self.table.heading("Description", text="Description")
        self.table.heading("Status", text="Status")
        self.table.column("Description", anchor="center", width=200)
        self.table.column("Status", anchor="center", width=100)
        self.table.pack(pady=10)

        # Load tasks from file
        self.load_tasks()

        # Display tasks in the table
        self.update_table()

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                content = file.read()
                if content:
                    self.tasks = json.loads(content)
                else:
                    self.tasks = []
        except FileNotFoundError:
            self.tasks = []
        except json.decoder.JSONDecodeError:
            messagebox.showerror("Error", "Error decoding JSON file. Please check the file format.")
        self.tasks = []


    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def update_table(self):
        self.table.delete(*self.table.get_children())
        for task in self.tasks:
            status = "Completed" if task["completed"] else "Not Completed"
            self.table.insert("", "end", values=(task["description"], status))

    def show_tasks(self):
        if not self.tasks:
            messagebox.showinfo("To-Do List", "No tasks found.")
        else:
            self.update_table()

    def add_task(self):
        description = simpledialog.askstring("Add Task", "Enter task description:")
        if description:
            task = {"description": description, "completed": False}
            self.tasks.append(task)
            self.update_table()
            self.save_tasks()
            messagebox.showinfo("Add Task", f"Task '{description}' added successfully.")

    def mark_task(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("Mark Task", "Please select a task.")
            return

        index = int(self.table.index(selected_item[0]))  # Get the index of the selected task
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_table()
            self.save_tasks()
            action = "marked as completed" if self.tasks[index]["completed"] else "marked as not completed"
            messagebox.showinfo("Mark Task", f"Task '{self.tasks[index]['description']}' {action}.")
        else:
            messagebox.showwarning("Mark Task", "Invalid task index.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
