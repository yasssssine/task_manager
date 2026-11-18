

def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']}")
        choice = input("Expense number to delete: ")
    if not choice.isdigit():
        print("Invalid expense number.")
        return

    index = int(choice) - 1
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Deleted: {removed['description']}")
    else:
        print("Invalid expense number.")


tasks = []

choice = ""
while choice != "0":

    print("\n--- TASK MANAGER ---")
    print("1. Add a task")
    print("2. Display tasks")
    print("3. Search for a task")
    print("4. Exit")
    print("5. Delete an expense")

    choice = input("Your choice: ")

    if choice == "1":
        task = input("Enter task title: ")

        if task == "":
            print("Task cannot be empty")
        else:
            tasks.append(task)
            print("Task added successfully")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

    elif choice == "3":
        keyword = input("Enter keyword: ")
        found = False

        for i in range(len(tasks)):
            if keyword.lower() in tasks[i].lower():
                print(i + 1, "-", tasks[i])
                found = True

        if found == False:
            print("Task not found")

    elif choice == "4":
        print("Goodbye!")
    elif choice == "5":
        delete_expense()

    else:
        print("Invalid choice")
