class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

def sort_employee_data(employees, sort_parameter):
    if sort_parameter == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif sort_parameter == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif sort_parameter == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        raise ValueError("Invalid sorting parameter")

def print_employee_data(employees):
    print("Employee ID   Name       Age   Salary")
    print("-------------------------------------")
    for emp in employees:
        print(f"{emp.emp_id}     {emp.name}    {emp.age}     {emp.salary}")

if __name__ == "__main__":
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    print("Select sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    sort_param = int(input("Enter your choice: "))

    sorted_employees = sort_employee_data(employees, sort_param)
    print_employee_data(sorted_employees)
