from tasks.ex9_register_person.person import Person


def _is_valid_salary(salary):
    if not salary.isdigit():
        raise ValueError("Salary cannot be negative and only numbers are allowed.")

    return salary


def _is_valid_role(role):
    if not role.isalpha():
        raise ValueError("Role should contains only alphabets")

    if len(role) > 20:
        raise ValueError("Role cannot exceed 20 characters.")

    return role


class Employee(Person):

    def __init__(self, name, last_name, age, gender, email, phone_number, salary, role):
        super().__init__(name, last_name, age, gender, email, phone_number)
        self.__salary = _is_valid_salary(salary)
        self.__role = _is_valid_role(role)

    @property
    def salary(self):
        return self.__salary

    @property
    def role(self):
        return self.__role

    def __str__(self) -> str:
        return str("Name: " + self.name + "\n" +
                   "Last Name: " + self.last_name + "\n" +
                   "Age: " + self.age + "\n" +
                   "Gender: " + self.gender + "\n" +
                   "Email: " + self.email + "\n" +
                   "Phone Number: " + self.phone_number + "\n" +
                   "Salary: " + self.salary + "\n" +
                   "Role: " + self.role)
