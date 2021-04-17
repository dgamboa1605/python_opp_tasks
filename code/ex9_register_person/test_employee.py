import pytest

from code.ex9_register_person.employee import Employee

name = "dennis"
las_name = "gamboa"
age = "30"
gender = "male"
email = "dennis.gamboa@gmail.com"
phone_number = "75992625"
salary = "12000"
role = "Manager"


class TestEmployee:
    def test_name_raise_exception_with_numbers(self):
        with pytest.raises(ValueError):
            b = Employee("dennis1", las_name, age, gender, email, phone_number, salary, role)
    
    def test_name_raise_exception_exceeds_20_characters(self):
        with pytest.raises(ValueError):
            b = Employee("dennisdennisdennisdennis", las_name, age, gender, email, phone_number, salary, role)
    
    def test_name_raise_exception_with_space(self):
        with pytest.raises(ValueError):
            b = Employee("dennis gamboa", las_name, age, gender, email, phone_number, salary, role)
        
    def test_name_raise_exception_with_invalid_characters(self):
        with pytest.raises(ValueError):
            b = Employee("dennisgamboa%&/", las_name, age, gender, email, phone_number, salary, role)
    
    def test_last_name_raise_exception_with_numbers(self):
        with pytest.raises(ValueError):
            b = Employee(name, "gamboa123", age, gender, email, phone_number, salary, role)
    
    def test_last_name_raise_exception_exceeds_20_characters(self):
        with pytest.raises(ValueError):
            b = Employee(name, "gamboagamboagamboagamboa", age, gender, email, phone_number, salary, role)
    
    def test_last_name_raise_exception_with_space(self):
        with pytest.raises(ValueError):
            b = Employee(name, "gamboa veliz", age, gender, email, phone_number, salary, role)
        
    def test_last_name_raise_exception_with_invalid_characters(self):
        with pytest.raises(ValueError):
            b = Employee(name, "gamboa%&$", age, gender, email, phone_number, salary, role)
    
    def test_age_raise_exception_with_letters(self):
        with pytest.raises(ValueError):
            b = Employee(name, las_name, "12asd", gender, email, phone_number, salary, role)
    
    def test_age_raise_exception_with_negative_numbers(self):
        with pytest.raises(ValueError):
            b = Employee(name, las_name, "-25", gender, email, phone_number, salary, role)
    
    def test_gender_raise_exception_with_numbers(self):
        with pytest.raises(ValueError):
            b = Employee(name, las_name, age, "male23", email, phone_number, salary, role)
    
    def test_gender_raise_exception_exceeds_20_characters(self):
        with pytest.raises(ValueError):
            b = Employee(name, las_name, age, "dennisdennisdennisdennis", email, phone_number, salary, role)
    
    def test_gender_raise_exception_with_space(self):
        with pytest.raises(ValueError):
            b = Employee(name, las_name, age, "dennis gamboa", email, phone_number, salary, role)
        
    def test_gender_raise_exception_with_invalid_characters(self):
        with pytest.raises(ValueError):
            b = Employee(name, las_name, age, "dennisgamboa%&/", email, phone_number, salary, role)
    
    def test_email_raise_exception_with_invalid_email(self):
        with pytest.raises(ValueError):
            b = Employee(name, las_name, age, gender, "dennis@test", phone_number, salary, role)
    
    def test_phone_number_raise_exception_with_letters(self):
        with pytest.raises(ValueError):
            b = Employee(name, las_name, age, gender, email, "12asd", salary, role)
    
    def test_phone_number_raise_exception_with_negative_numbers(self):
        with pytest.raises(ValueError):
            b = Employee(name, las_name, age, gender, email, "-25345345", salary, role)
    
    def test_salary_raise_exception_with_letters(self):
        with pytest.raises(ValueError):
            b = Employee(name, las_name, age, gender, email, phone_number, "12asd", role)
    
    def test_salary_raise_exception_with_negative_numbers(self):
        with pytest.raises(ValueError):
            b = Employee(name, las_name, age, gender, email, phone_number, "-25345345", role)
    
    def test_role_raise_exception_with_numbers(self):
        with pytest.raises(ValueError):
            b = Employee(name, las_name, age, gender, email, phone_number, salary, "dennis1")
    
    def test_role_raise_exception_exceeds_20_characters(self):
        with pytest.raises(ValueError):
            b = Employee(name, las_name, age, gender, email, phone_number, salary, "dennisdennisdennisdennis")
    
    def test_role_raise_exception_with_space(self):
        with pytest.raises(ValueError):
            b = Employee(name, las_name, age, gender, email, phone_number, salary, "dennis gamboa")
        
    def test_role_raise_exception_with_invalid_characters(self):
        with pytest.raises(ValueError):
            b = Employee(name, las_name, age, gender, email, phone_number, salary, "dennisgamboa%&/")
