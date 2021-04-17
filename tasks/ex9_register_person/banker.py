from tasks.ex9_register_person.employee import Employee


class Banker(Employee):
    def __init__(self, name, last_name, age, gender, email, phone_number, salary, role="Banker"):
        super().__init__(name, last_name, age, gender, email, phone_number, salary, role)

    def __str__(self) -> str:
        return super().__str__()
