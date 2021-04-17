from code.ex9_register_person.register_person import RegisterPerson

res = RegisterPerson()
res.register_customer(1)
res.register_employee(1)


class TestRegisterPerson:

    def test_register_customer(self):
        assert 1 == len(res.customer)
    
    def test_register_employee(self):
        assert 1 == len(res.employee)
    
    def test_print_customer(self):
        assert '1' == res.print_customer()
    
    def test_print_employee(self):
        assert '1' == res.print_employee()
