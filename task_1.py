# Simple To-Do List Application in Python

tasks = []                 # List to store tasks

def show_menu():
    print("\n--- TO-DO LIST MENU ---")  # Display the menu options
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():          # Function to display all tasks
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():          # Function to add a new task
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def update_task():          # Function to update an existing task
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter task number to update: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter updated task: ")
                tasks[task_num - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():          # Function to delete a task
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()














