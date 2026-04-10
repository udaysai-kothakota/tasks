import json
import os

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add task
def add_task():
    title = input("Enter task: ")
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("✅ Task added!")

# View tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. {task['title']} [{status}]")

# Mark complete
def complete_task():
    tasks = load_tasks()
    view_tasks()

    try:
        num = int(input("Enter task number to mark complete: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("🎉 Task marked as completed!")
    except:
        print("Invalid input.")

# Delete task
def delete_task():
    tasks = load_tasks()
    view_tasks()

    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"🗑 Deleted: {removed['title']}")
    except:
        print("Invalid input.")

# CLI Menu
def main():
    while True:
        print("\n==== TASK TRACKER ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()