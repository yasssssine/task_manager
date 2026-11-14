
tasks = []

choice = ""
while choice != "0":

    print("\n--- TASK MANAGER ---")
    print("1. Add a task")
    print("2. Display tasks")
    print("3. Search for a task")
    print("0. Exit")

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

    elif choice == "0":
        print("Goodbye!")

    else:
        print("Invalid choice")
