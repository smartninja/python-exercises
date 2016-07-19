class Task:
    name = "default name"
    completed = False
    due_date = "31-FEB-2000"

    def __init__(self, task_name, task_status, task_due_date):
        self.name = task_name
        self.completed = task_status
        self.due_date = task_due_date


def main():
    todo_file = open("toy-company-todo.txt", "r+")

    task_list = []

    for item in todo_file:
        task_name, status, due_date = item.split(";")

        task = Task(task_name=task_name, task_status=status, task_due_date=due_date)

        task_list.append(task)

    action = raw_input("Would you like to see a list of existing tasks, update tasks or ad a new one? (list/update/new) ")

    if action == "list":
        list_of_tasks(task_list)
    elif action == "update":
        update_tasks(task_list)

    todo_file.close()


def list_of_tasks(tasks):
    for item in tasks:
        print("TASK: " + item.name)
        print("Completed: " + item.completed)
        print("Due date: " + item.due_date)


def update_tasks(tasks):
    for item in tasks:
        print("TASK: " + item.name)
        print("Completed: " + item.completed)
        print("Due date: " + item.due_date)

        edit = raw_input("Would you like to edit this task? (yes/no) ")

        if edit == "yes":
            new_name = raw_input("Enter new task name (press enter to skip): ")

            if new_name:  # this is example only for changing task name. Status and due date have the same logic.
                item.name = new_name
                print("Task name successfully changed")
        else:
            continue


if __name__ == "__main__":
    main()
    print("END")
