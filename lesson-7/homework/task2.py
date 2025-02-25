class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename

    def add_employee(self, employee):
        with open(self.filename, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        try:
            with open(self.filename, "r") as file:
                employees = file.readlines()
                if employees:
                    print("Employee Records:")
                    for emp in employees:
                        print(emp.strip())
                else:
                    print("No employee records found.")
        except FileNotFoundError:
            print("No employee records found.")

    def search_employee(self, employee_id):
        try:
            with open(self.filename, "r") as file:
                employees = file.readlines()
                for emp in employees:
                    emp_data = emp.strip().split(", ")
                    if emp_data[0] == employee_id:
                        print("Employee Found:")
                        print(emp.strip())
                        return
                print("Employee not found.")
        except FileNotFoundError:
            print("No employee records found.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        try:
            with open(self.filename, "r") as file:
                employees = file.readlines()
            with open(self.filename, "w") as file:
                for emp in employees:
                    emp_data = emp.strip().split(", ")
                    if emp_data[0] == employee_id:
                        if name:
                            emp_data[1] = name
                        if position:
                            emp_data[2] = position
                        if salary:
                            emp_data[3] = salary
                        emp = ", ".join(emp_data) + "\n"
                    file.write(emp)
            print("Employee updated successfully!")
        except FileNotFoundError:
            print("No employee records found.")

    def delete_employee(self, employee_id):
        try:
            with open(self.filename, "r") as file:
                employees = file.readlines()
            with open(self.filename, "w") as file:
                for emp in employees:
                    emp_data = emp.strip().split(", ")
                    if emp_data[0] != employee_id:
                        file.write(emp)
            print("Employee deleted successfully!")
        except FileNotFoundError:
            print("No employee records found.")

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                employee = Employee(employee_id, name, position, salary)
                self.add_employee(employee)
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ")
                self.search_employee(employee_id)
            elif choice == "4":
                employee_id = input("Enter Employee ID to update: ")
                name = input("Enter new Name (leave blank to keep current): ")
                position = input("Enter new Position (leave blank to keep current): ")
                salary = input("Enter new Salary (leave blank to keep current): ")
                self.update_employee(employee_id, name, position, salary)
            elif choice == "5":
                employee_id = input("Enter Employee ID to delete: ")
                self.delete_employee(employee_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
