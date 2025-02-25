import json
import csv


class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


class TaskManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for task in self.tasks:
                print(task)
        else:
            print("No tasks found.")

    def update_task(
        self, task_id, title=None, description=None, due_date=None, status=None
    ):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if status:
                    task.status = status
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if filtered_tasks:
            print("Filtered Tasks:")
            for task in filtered_tasks:
                print(task)
        else:
            print("No tasks found with the given status.")

    def save_tasks(self):
        self.storage.save_tasks(self.tasks)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.storage.load_tasks()
        print("Tasks loaded successfully!")


class Storage:
    def save_tasks(self, tasks):
        raise NotImplementedError

    def load_tasks(self):
        raise NotImplementedError


class CSVStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def save_tasks(self, tasks):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            for task in tasks:
                writer.writerow(
                    [
                        task.task_id,
                        task.title,
                        task.description,
                        task.due_date,
                        task.status,
                    ]
                )

    def load_tasks(self):
        tasks = []
        try:
            with open(self.filename, mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    task_id, title, description, due_date, status = row
                    tasks.append(Task(task_id, title, description, due_date, status))
        except FileNotFoundError:
            pass
        return tasks


class JSONStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def save_tasks(self, tasks):
        with open(self.filename, "w") as file:
            json.dump([task.__dict__ for task in tasks], file)

    def load_tasks(self):
        tasks = []
        try:
            with open(self.filename, "r") as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    tasks.append(Task(**task_data))
        except FileNotFoundError:
            pass
        return tasks


if __name__ == "__main__":
    storage_choice = input("Choose storage format (1 for CSV, 2 for JSON): ")
    if storage_choice == "1":
        storage = CSVStorage("tasks.csv")
    elif storage_choice == "2":
        storage = JSONStorage("tasks.json")
    else:
        print("Invalid choice. Defaulting to CSV.")
        storage = CSVStorage("tasks.csv")

    manager = TaskManager(storage)

    while True:
        print("\nWelcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            task = Task(task_id, title, description, due_date, status)
            manager.add_task(task)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new Title (leave blank to keep current): ")
            description = input("Enter new Description (leave blank to keep current): ")
            due_date = input("Enter new Due Date (leave blank to keep current): ")
            status = input("Enter new Status (Pending/In Progress/Completed): ")
            manager.update_task(task_id, title, description, due_date, status)
        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            manager.delete_task(task_id)
        elif choice == "5":
            status = input(
                "Enter Status to filter by (Pending/In Progress/Completed): "
            )
            manager.filter_tasks(status)
        elif choice == "6":
            manager.save_tasks()
        elif choice == "7":
            manager.load_tasks()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")