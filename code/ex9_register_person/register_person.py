
class RegisterPerson:

    def __init__(self):
        self.__customer = []
        self.__employee = []
    
    def register_customer(self, customer):
        self.__customer.append(customer)
    
    def register_employee(self, employee):
        self.__employee.append(employee)
    
    def print_customer(self):
        for i in self.__customer:
            return str(i)
    
    def print_employee(self):
        for i in self.__employee:
            return str(i)

    @property
    def customer(self):
        return self.__customer
    
    @property
    def employee(self):
        return self.__employee
