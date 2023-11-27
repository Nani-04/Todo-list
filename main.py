# todo.py

def show_menu():
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Save and Quit")

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

def main():
    todo_list = load_from_file()

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            new_task = input("Enter the new task: ")
            add_task(todo_list, new_task)
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as done: "))
            mark_task_as_done(todo_list, task_index)
        elif choice == "4":
            save_to_file(todo_list)
            print("To-Do List saved. Quitting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
