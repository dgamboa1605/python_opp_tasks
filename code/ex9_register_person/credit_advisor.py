from code.ex9_register_person.employee import Employee


class CreditAdvisor(Employee):
    def __init__(self, name, last_name, age, gender, email, phone_number, salary, role="CreditAdvisor"):
        super().__init__(name, last_name, age, gender, email, phone_number, salary, role)
    
    def __str__(self) -> str:
        return super().__str__()
