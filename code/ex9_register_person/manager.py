from code.ex9_register_person.employee import Employee


class Manager(Employee):
    def __init__(self, name, last_name, age, gender, email, phone_number, salary, role="Manager"):
        super().__init__(name, last_name, age, gender, email, phone_number, salary, role)

    def __str__(self) -> str:
        return super().__str__()
