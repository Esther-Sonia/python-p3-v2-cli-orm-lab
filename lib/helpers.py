from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    from models.employee import Employee
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    from models.employee import Employee
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")


def find_employee_by_id():
    from models.employee import Employee
    try:
        id = int(input("Enter the employee's id: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    employee = Employee.find_by_id(id)
    if employee:
        print(employee)
    else:
        print(f"Employee {id} not found")


def create_employee():
    from models.employee import Employee
    name = input("Enter the employee's name: ").strip()
    job_title = input("Enter the employee's job title: ").strip()
    try:
        department_id = int(input("Enter the employee's department id: "))
    except ValueError:
        print("Invalid department id")
        return

    try:
        employee = Employee.create(name, job_title, department_id)
        print(f"Success: {employee}")
    except Exception as e:
        print("Error creating employee: ", e)



def update_employee():
    from models.employee import Employee
    try:
        id = int(input("Enter the employee's id: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    employee = Employee.find_by_id(id)
    if not employee:
        print(f"Employee {id} not found")
        return

    name = input("Enter the employee's new name: ").strip()
    job_title = input("Enter the employee's new job title: ").strip()
    try:
        department_id = int(input("Enter the employee's new department id: "))
    except ValueError:
        print("Invalid department id")
        return

    try:
        employee.name = name
        employee.job_title = job_title
        employee.department_id = department_id
        employee.update()
        print(f"Success: {employee}")
    except Exception as e:
        print("Error updating employee: ", e)


def delete_employee():
    from models.employee import Employee
    try:
        id = int(input("Enter the employee's id: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    employee = Employee.find_by_id(id)
    if not employee:
        print(f"Employee {id} not found")
        return

    employee.delete()
    print(f"Employee {id} deleted")


def list_department_employees():
    from models.department import Department
    try:
        department_id = int(input("Enter the department's id: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    department = Department.find_by_id(department_id)
    if not department:
        print(f"Department {department_id} not found")
        return

    employees = department.employees()
    for employee in employees:
        print(employee)