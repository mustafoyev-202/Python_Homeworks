def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)

    return wrapper


@check
def div(a, b):
    return a / b


def create_file():
    with open("employees.txt", "w") as file:
        pass


def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")


def view_employees():
    with open("employees.txt", "r") as file:
        for line in file:
            print(line.strip())


def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    with open("employees.txt", "r") as file:
        for line in file:
            if line.startswith(emp_id):
                print(line.strip())
                return
    print("Employee not found")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    lines = []
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    with open("employees.txt", "w") as file:
        for line in lines:
            if line.startswith(emp_id):
                name = input("Enter new Name: ")
                position = input("Enter new Position: ")
                salary = input("Enter new Salary: ")
                file.write(f"{emp_id}, {name}, {position}, {salary}\n")
            else:
                file.write(line)


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    lines = []
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    with open("employees.txt", "w") as file:
        for line in lines:
            if not line.startswith(emp_id):
                file.write(line)


def main():
    create_file()
    while True:
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    main()
