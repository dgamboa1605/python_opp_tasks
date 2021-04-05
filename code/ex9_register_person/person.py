import re

class Person:
    def __init__(self, name, last_name, age, gender, email, phone_number):
        self.__name = self._is_valid_name(name)
        self.__last_name = self._is_valid_last_name(last_name)
        self.__age = self._is_valid_age(age)
        self.__gender = self._is_valid_gender(gender)
        self.__email = self._is_valid_email(email)
        self.__phone_number = self._is_valid_phone_number(phone_number)

    @property
    def name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def age(self):
        return self.__age
    
    @property
    def gender(self):
        return self.__gender
    
    @property
    def email(self):
        return self.__email
    
    @property
    def phone_number(self):
        return self.__phone_number
    
    def _is_valid_name(self, name):
        if not name.isalpha():
            raise ValueError("Name should contains only alphabets")

        if len(name) > 20:
            raise ValueError("Name cannot exceed 20 characters.")

        return name
    
    def _is_valid_last_name(self, last_name):
        if not last_name.isalpha():
            raise ValueError("Last Name should contains only alphabets")

        if len(last_name) > 20:
            raise ValueError("Last Name cannot exceed 20 characters.")

        return last_name
    
    def _is_valid_age(self, age):
        if not age.isdigit():
             raise ValueError("Age cannot be negative and only numbers are allowed.")

        return age
    
    def _is_valid_gender(self, gender):
        if not gender.isalpha():
            raise ValueError("Gender should contains only alphabets")
            
        if len(gender) > 20:
            raise ValueError("Gender cannot exceed 20 characters.")

        return gender
    
    def _is_valid_email(self, email):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(regex, email):
            raise ValueError("It's not an email address.")

        return email
    
    def _is_valid_phone_number(self, phone_number):
        if not phone_number.isdigit():
             raise ValueError("Phone Number cannot be negative and only numbers are allowed.")

        return phone_number
