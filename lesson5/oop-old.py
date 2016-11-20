class Task:
    def __init__(self, task_name, task_status, task_due_date):
        self.name = task_name
        self.completed = task_status
        self.due_date = task_due_date


def main():
    todo_file = open("toy-company-todo.txt", "r")

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
    elif action == "new":
        add_new_task(task_list)
    else:
        print "Sorry, your input was incorrect. Please try again."

    save_changes(task_list, todo_file)
    todo_file.close()


def list_of_tasks(tasks):
    for index, item in enumerate(tasks):
        print str(index) + ") TASK: " + item.name
        print "Completed: " + item.completed
        print "Due date: " + item.due_date


def update_tasks(tasks):
    list_of_tasks(tasks)

    task_index = int(raw_input("Enter the index number of the task you'd like to edit: "))

    task = tasks[task_index]

    print "You selected: "
    print "TASK: " + task.name
    print "Completed: " + task.completed
    print "Due date: " + task.due_date

    # this is example only for changing task name. Status and due date have the same logic.
    new_name = raw_input("Enter new task name (press enter to skip): ")
    task.name = new_name
    print "Task name successfully changed"


def add_new_task(tasks):
    task_name = raw_input("Enter the name of the task: ")
    task_status = raw_input("Was the task completed yet? (True/False) ")
    due_date = raw_input("Enter the due date (in this format: 05-MAR-2017): ")

    new_task = Task(task_name="\n"+task_name, task_status=task_status, task_due_date=due_date)  # \n means new line. This will be helpful when saving tasks back to TXT file.

    tasks.append(new_task)

    print "New task was successfully added!"


def save_changes(tasks, todo_file):
    todo_file.close()
    todo_file = open("toy-company-todo.txt", "w")

    for item in tasks:
        todo_file.write(item.name + ";" + item.completed + ";" + item.due_date)


if __name__ == "__main__":
    main()
    print "END"
