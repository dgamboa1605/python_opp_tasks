import pytest

from code.ex9_register_person.customer import Customer

name = "dennis"
las_name = "Gamboa"
age = "30"
gender = "male"
email = "dennis.gamboa@gmail.com"
phone_number = "75992625"


class TestCustomer:
    def test_name_raise_exception_with_numbers(self):
        with pytest.raises(ValueError):
            b = Customer("dennis1", las_name, age, gender, email, phone_number)
    
    def test_name_raise_exception_exceeds_20_characters(self):
        with pytest.raises(ValueError):
            b = Customer("dennisdennisdennisdennis", las_name, age, gender, email, phone_number)
    
    def test_name_raise_exception_with_space(self):
        with pytest.raises(ValueError):
            b = Customer("dennis gamboa", las_name, age, gender, email, phone_number)
        
    def test_name_raise_exception_with_invalid_characters(self):
        with pytest.raises(ValueError):
            b = Customer("dennisgamboa%&/", las_name, age, gender, email, phone_number)
    
    def test_last_name_raise_exception_with_numbers(self):
        with pytest.raises(ValueError):
            b = Customer(name, "gamboa123", age, gender, email, phone_number)
    
    def test_last_name_raise_exception_exceeds_20_characters(self):
        with pytest.raises(ValueError):
            b = Customer(name, "gamboagamboagamboagamboa", age, gender, email, phone_number)
    
    def test_last_name_raise_exception_with_space(self):
        with pytest.raises(ValueError):
            b = Customer(name, "gamboa veliz", age, gender, email, phone_number)
        
    def test_last_name_raise_exception_with_invalid_characters(self):
        with pytest.raises(ValueError):
            b = Customer(name, "gamboa%&$", age, gender, email, phone_number)
    
    def test_age_raise_exception_with_letters(self):
        with pytest.raises(ValueError):
            b = Customer(name, las_name, "12asd", gender, email, phone_number)
    
    def test_age_raise_exception_with_negative_numbers(self):
        with pytest.raises(ValueError):
            b = Customer(name, las_name, "-25", gender, email, phone_number)
    
    def test_gender_raise_exception_with_numbers(self):
        with pytest.raises(ValueError):
            b = Customer(name, las_name, age, "male23", email, phone_number)
    
    def test_gender_raise_exception_exceeds_20_characters(self):
        with pytest.raises(ValueError):
            b = Customer(name, las_name, age, "dennisdennisdennisdennis", email, phone_number)
    
    def test_gender_raise_exception_with_space(self):
        with pytest.raises(ValueError):
            b = Customer(name, las_name, age, "dennis gamboa", email, phone_number)
        
    def test_gender_raise_exception_with_invalid_characters(self):
        with pytest.raises(ValueError):
            b = Customer(name, las_name, age, "dennisgamboa%&/", email, phone_number)
    
    def test_email_raise_exception_with_invalid_email(self):
        with pytest.raises(ValueError):
            b = Customer(name, las_name, age, gender, "dennis@test", phone_number)
    
    def test_phone_number_raise_exception_with_letters(self):
        with pytest.raises(ValueError):
            b = Customer(name, las_name, age, gender, email, "12asd")
    
    def test_phone_number_raise_exception_with_negative_numbers(self):
        with pytest.raises(ValueError):
            b = Customer(name, las_name, age, gender, email, "-25345345")
