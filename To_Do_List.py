todo_list = []

def menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

while True:
    menu()
    option = input("Enter your choice (1-4): ")
    if option == '1':
        if not todo_list:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
    elif option == '2':
        task = input("Enter new task: ")
        if task.strip():
            todo_list.append(task)
            print("Task added!")
        else:
            print("Cannot add an empty task.")
    elif option == '3':
        try:
            task_no = int(input("Enter task number to delete: "))
            if 0 < task_no <= len(todo_list):
                removed = todo_list.pop(task_no - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
    elif option == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
