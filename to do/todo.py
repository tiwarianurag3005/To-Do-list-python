import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def main():
    tasks = load_tasks()

    while True:
        print("===== TO-DO LIST =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            task = input("Enter new task: ")
            tasks.append("[ ] " + task)
            save_tasks(tasks)
            print("Task added!\n")
        elif choice == '3':
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                if tasks[index].startswith("[ ]"):
                    tasks[index] = tasks[index].replace("[ ]", "[✔]")
                    save_tasks(tasks)
                    print("Task marked as done!\n")
                else:
                    print("Task already completed.\n")
            except:
                print("Invalid task number.\n")
        elif choice == '4':
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f"Deleted: {removed}\n")
            except:
                print("Invalid task number.\n")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
