import tkinter as tk
from tkinter import messagebox


class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Initialize tasks list
        self.tasks = []

        # Create frame to contain task listbox and checkbuttons
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Create task listbox with associated checkbuttons
        self.task_listbox = tk.Listbox(self.frame, height=15, width=50, bg='lightblue')
        self.task_listbox.pack(side=tk.LEFT, padx=5)

        self.check_buttons = []
        for _ in range(10):  # Create 10 checkboxes by default
            check_button = tk.Checkbutton(self.frame, command=self.toggle_task)
            self.check_buttons.append(check_button)

        # Create scrollbar for task listbox
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        # Create entry for new task
        self.new_task_entry = tk.Entry(root, width=50, bg='lightcoral')
        self.new_task_entry.pack(pady=10)

        # Create buttons
        self.add_button = tk.Button(root, text="Add Task", bg='lightgreen', command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10)
        self.remove_button = tk.Button(root, text="Remove Task", bg='lightgreen', command=self.remove_task)
        self.remove_button.pack(side=tk.LEFT, padx=10)
        self.clear_button = tk.Button(root, text="Clear All", bg='lightgreen', command=self.clear_tasks)
        self.clear_button.pack(side=tk.LEFT, padx=10)

        # Add buttons for extra features
        self.save_button = tk.Button(root, text="Save Tasks", bg='lightgreen', command=self.save_tasks)
        self.save_button.pack(side=tk.LEFT, padx=10)
        self.load_button = tk.Button(root, text="Load Tasks", bg='lightgreen', command=self.load_tasks)
        self.load_button.pack(side=tk.LEFT, padx=10)
        self.about_button = tk.Button(root, text="About", bg='lightgreen', command=self.show_about)
        self.about_button.pack(side=tk.LEFT, padx=10)

        # Load tasks from file if exists
        self.load_tasks()

    def add_task(self):
        task = self.new_task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.new_task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def clear_tasks(self):
        self.tasks = []
        self.task_listbox.delete(0, tk.END)
        self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
        messagebox.showinfo("Saved", "Tasks have been saved successfully.")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    task = line.strip()
                    self.tasks.append(task)
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

    def show_about(self):
        messagebox.showinfo("About", "To-Do List App\nVersion 1.0\nCreated by Your Yashas")

    def toggle_task(self):
        selected_indices = self.task_listbox.curselection()
        for idx, button in enumerate(self.check_buttons):
            if idx in selected_indices:
                button.select()
            else:
                button.deselect()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
