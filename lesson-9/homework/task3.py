import json
import csv


# Load tasks from tasks.json
def load_tasks(filename="tasks.json"):
    with open(filename, "r") as file:
        tasks = json.load(file)
    return tasks


# Display all tasks
def display_tasks(tasks):
    for task in tasks:
        print(
            f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}"
        )


# Save tasks to tasks.json
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)


# Calculate task completion stats
def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(task["completed"] for task in tasks)
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task["priority"] for task in tasks) / total_tasks
    return total_tasks, completed_tasks, pending_tasks, average_priority


# Convert JSON data to CSV
def convert_to_csv(tasks, filename="tasks.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow(
                [task["id"], task["task"], task["completed"], task["priority"]]
            )


# Main program
if __name__ == "__main__":
    tasks = load_tasks()
    display_tasks(tasks)
    total_tasks, completed_tasks, pending_tasks, average_priority = calculate_stats(
        tasks
    )
    print(f"\nTotal tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")
    convert_to_csv(tasks)
