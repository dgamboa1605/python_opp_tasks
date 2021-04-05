from manager import Manager

name = "dennis"
last_name = "gamboa"
age = "30"
gender = "male"
email = "dennis.gamboa@gmail.com"
phone_number = "75992625"
salary = "12000"

class TestManager:
    def test_print_str(self):
        res = "Name: dennis\nLast Name: gamboa\nAge: 30\nGender: male\nEmail: dennis.gamboa@gmail.com\nPhone Number: 75992625\nSalary: 12000\nRole: Manager"
        b = Manager(name, last_name, age, gender, email, phone_number, salary)
        assert str(b) == res
    