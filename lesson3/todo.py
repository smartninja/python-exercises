print("Welcome to the TO-DO task management program.")

todo_dict = {}

while True:
    task = raw_input("Please enter a TO-DO task: ")
    status = raw_input("Was the task completed yet? (yes/no) ")
    print("Your task is: " + task)

    if status == "yes":
        todo_dict[task] = True  # this is how we add a key-value pair into a dict
    else:
        todo_dict[task] = False

    new = raw_input("Would you like to enter new task? (yes/no) ")

    if new == "no":
        break

print("All tasks: %s" % todo_dict)

print("Completed tasks:")
for item in todo_dict:
    if todo_dict[item] is True:
        print("- " + item)

print("Incomplete tasks:")
for item in todo_dict:
    if todo_dict[item] is False:
        print("- " + item)

print("END")
