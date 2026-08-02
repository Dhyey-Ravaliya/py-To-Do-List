print("                                                                     To-Do List                                                               ")

while True:

    add_task = input("You Want To Add New Task (y/n): ").lower()
    if add_task == "y":
        new_task = input("Task:~ ")
        with open("tasks.txt", "a") as f:
            f.write(new_task + "\n")

    elif add_task == "n":
        pre_tasks = input("You want To See Previous Tasks (y/n): ").lower()
        if pre_tasks == "y":
            with open("tasks.txt") as f:
                print(f.read())

        elif pre_tasks == "n":
            print("Thanks, Bye")
            break
        else:
            print("INVALID VALUE ENTERED")
    else:
        print("INVALID VALUE ENTERED")
