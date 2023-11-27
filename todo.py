import tkinter as tk
from tkinter import messagebox


def show_menu():
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Mark Multiple Tasks as Done")
    print("5. Save and Quit")
    print("6. Show Percentage of Tasks Completed")
    print("7. Show Number of Tasks Pending")
    print("8. Daily Time")
    print("9. Steps Count")
    print("10. Take Break")
    print("11. Remind to Drink Water")
    print("12. Quit")


def view_todo_list(todo_list):
    print("\n--- To-Do List ---")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")
    print()


def add_task(todo_list, new_task):
    todo_list.append(new_task)
    print(f"Task '{new_task}' added successfully!")


def mark_task_as_done(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        task = todo_list.pop(task_index - 1)
        print(f"Task '{task}' marked as done!")
    else:
        print("Invalid task index. Please try again.")


def mark_multiple_tasks_as_done(todo_list, task_indices):
    completed_tasks = []
    for index in task_indices:
        if 1 <= index <= len(todo_list):
            completed_tasks.append(todo_list[index - 1])
            todo_list[index - 1] = f"[Done] {todo_list[index - 1]}"
        else:
            print(f"Invalid task index {index}. Skipping.")

    if completed_tasks:
        print(f"Marked tasks as done: {', '.join(completed_tasks)}")
    else:
        print("No tasks marked as done.")


def save_to_file(todo_list, filename="todo_list.txt"):
    with open(filename, "w") as file:
        for task in todo_list:
            file.write(task + "\n")


def load_from_file(filename="todo_list.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ToDo App")

        self.todo_list = load_from_file()

        self.create_widgets()

    def create_widgets(self):
        # Task Entry
        self.task_entry = tk.Entry(self.master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task Button
        add_task_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        add_task_button.grid(row=0, column=1, padx=10, pady=10)

        # Show Tasks Button
        show_tasks_button = tk.Button(self.master, text="Show Tasks", command=self.show_tasks)
        show_tasks_button.grid(row=1, column=0, padx=10, pady=10)

        # Mark All Tasks as Complete Button
        mark_all_button = tk.Button(self.master, text="Mark All Complete", command=self.mark_all_complete)
        mark_all_button.grid(row=1, column=1, padx=10, pady=10)

        # Show Percentage of Tasks Completed
        show_percentage_button = tk.Button(self.master, text="Show Percentage", command=self.show_percentage)
        show_percentage_button.grid(row=2, column=0, padx=10, pady=10)

        # Show Number of Tasks Pending
        show_pending_button = tk.Button(self.master, text="Show Pending Tasks", command=self.show_pending)
        show_pending_button.grid(row=2, column=1, padx=10, pady=10)

        # Daily Time
        daily_time_button = tk.Button(self.master, text="Daily Time", command=self.daily_time)
        daily_time_button.grid(row=3, column=0, padx=10, pady=10)

        # Steps Count
        steps_count_button = tk.Button(self.master, text="Steps Count", command=self.steps_count)
        steps_count_button.grid(row=3, column=1, padx=10, pady=10)

        # Take Break
        take_break_button = tk.Button(self.master, text="Take Break", command=self.take_break)
        take_break_button.grid(row=4, column=0, padx=10, pady=10)

        # Remind to Drink Water
        remind_water_button = tk.Button(self.master, text="Remind to Drink Water", command=self.remind_water)
        remind_water_button.grid(row=4, column=1, padx=10, pady=10)

        # Quit Button
        quit_button = tk.Button(self.master, text="Quit", command=self.quit_app)
        quit_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_task(self):
        new_task = self.task_entry.get()
        if new_task:
            add_task(self.todo_list, new_task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def show_tasks(self):
        view_todo_list(self.todo_list)

    def mark_all_complete(self):
        mark_multiple_tasks_as_done(self.todo_list, range(1, len(self.todo_list) + 1))

    def show_percentage(self):
        total_tasks = len(self.todo_list)
        completed_tasks = sum(1 for task in self.todo_list if task.startswith("[Done]"))
        if total_tasks > 0:
            percentage = (completed_tasks / total_tasks) * 100
            messagebox.showinfo("Percentage Complete", f"Percentage of tasks completed: {percentage:.2f}%")
        else:
            messagebox.showinfo("Percentage Complete", "No tasks available.")

    def show_pending(self):
        pending_tasks = sum(1 for task in self.todo_list if not task.startswith("[Done]"))
        messagebox.showinfo("Pending Tasks", f"Number of tasks pending: {pending_tasks}")

    def daily_time(self):
        # Placeholder for daily time functionality
        messagebox.showinfo("Daily Time", "Placeholder for daily time functionality.")

    def steps_count(self):
        # Placeholder for steps count functionality
        messagebox.showinfo("Steps Count", "Placeholder for steps count functionality.")

    def take_break(self):
        # Placeholder for take break functionality
        messagebox.showinfo("Take Break", "Placeholder for take break functionality.")

    def remind_water(self):
        # Placeholder for remind to drink water functionality
        messagebox.showinfo("Remind to Drink Water", "Placeholder for remind to drink water functionality.")

    def quit_app(self):
        save_to_file(self.todo_list)
        self.master.destroy()


def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
