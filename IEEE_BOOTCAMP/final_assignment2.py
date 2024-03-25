
class task:
    def __init__(self, title, description, due_date):  # to construct object of task
        self.title = title
        self.description = description
        self.due_date = due_date
        self.is_complete = "Not completed yet"

    def mark_as_completed(self):  # method to mark task as completed
        self.is_complete = "Yeah! Completed"

    def __str__(self):  # special method to print task as a formatted output
        return f"Title of task: {self.title}" \
               f"\nDescription: {self.description}" \
               f"\ndue date : {self.due_date}" \
               f"\nStatus : {self.is_complete}"


class taskManager:
    def __init__(self):
        self.tasks = []  # create an empty list

    def add_task(self, tasks):
        self.tasks.append(tasks)  # to add new task to the list

    def view_tasks(self):  # to view all the task
        if len(self.tasks) == 0:
            print("Yeah! No Task")
            return
        for i in range(len(self.tasks)):
            print(f"Task {i + 1}:\n{self.tasks[i]}")

    def mark_task_as_completed(self, task_number):
        try:
            self.tasks[task_number].mark_as_completed()
            print(f"Task number {task_number + 1} marked as complete.")
        except IndexError:
            print("Invalid task number.")


def menu(task_manager):
    print("1. Add Task\n2. View Task\n3. Mark task as completed\n4. Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        task_manager.add_task(task(title=input("Enter Title : "),
                                   description=input("Enter Task Description : "),
                                   due_date=input("Enter Due date format(dd/mm/yyyy) : ")))
        print("Task Added successfully.")
    elif choice == 2:
        task_manager.view_tasks()
    elif choice == 3:
        if len(task_manager.tasks) == 0:
            print("No task to do!")
            return
        task_manager.view_tasks()
        temp = int(input(f"Enter Task Number to mark as completed : "))
        task_manager.mark_task_as_completed(temp - 1)
    elif choice == 4:
        exit()
    else:
        print("Invalid Input")


def main():
    task_manager = taskManager()
    while True:
        menu(task_manager)


if __name__ == "__main__":
    main()
