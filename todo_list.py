# todo_list.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def update_task(self, task_number, new_task):
        try:
            task_number = int(task_number)
            if task_number < 1 or task_number > len(self.tasks):
                print("Invalid task number.")
            else:
                self.tasks[task_number - 1] = new_task
                print(f"Task {task_number} updated to '{new_task}'.")
        except ValueError:
            print("Invalid task number.")

    def delete_task(self, task_number):
        try:
            task_number = int(task_number)
            if task_number < 1 or task_number > len(self.tasks):
                print("Invalid task number.")
            else:
                del self.tasks[task_number - 1]
                print(f"Task {task_number} deleted.")
        except ValueError:
            print("Invalid task number.")

def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            task_number = input("Enter the task number to update: ")
            new_task = input("Enter the new task: ")
            todo.update_task(task_number, new_task)
        elif choice == "4":
            task_number = input("Enter the task number to delete: ")
            todo.delete_task(task_number)
        elif choice == "5":
            print("Have a great day, Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()