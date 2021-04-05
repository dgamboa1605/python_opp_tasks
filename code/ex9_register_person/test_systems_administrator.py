from systems_administrator import SystemsAdministrator

name = "dennis"
last_name = "gamboa"
age = "30"
gender = "male"
email = "dennis.gamboa@gmail.com"
phone_number = "75992625"
salary = "12000"

class TestSystemsAdministrator:
    def test_print_str(self):
        res = "Name: dennis\nLast Name: gamboa\nAge: 30\nGender: male\nEmail: dennis.gamboa@gmail.com\nPhone Number: 75992625\nSalary: 12000\nRole: SystemsAdministrator"
        b = SystemsAdministrator(name, last_name, age, gender, email, phone_number, salary)
        assert str(b) == res
    