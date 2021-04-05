from employee import Employee

class SystemsAdministrator(Employee):
    def __init__(self, name, last_name, age, gender, email, phone_number, salary, role="SystemsAdministrator"):
        super().__init__(name, last_name, age, gender, email, phone_number, salary, role)
    
    def __str__(self) -> str:
        return super().__str__()
