class Student:
    
    def __init__(self, name: str, lastname: str, year: int, country: str, occupation: str):
        self.__name = name
        self.__lastname = lastname
        self.__year = year
        self.__country = country
        self.__occupation = occupation

    def presentation(self):
        print("My name is {} {}, I'm from {}, I'm {} years old and I'm {}".format(self.name, self.lastname, self.country, self.year, self.occupation))

        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, new_lastname):
        self.__lastname = new_lastname
    
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year
    
    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, new_country):
        self.__country = new_country
    
    @property
    def occupation(self):
        return self.__occupation

    @occupation.setter
    def occupation(self, new_occupation):
        self.__occupation = new_occupation


name = input("[+] Enter your name: ")
print("Entered: {} Name".format(name))
lastname = input("[+] Enter your latname: ")
print("Entered: {} lastname".format(lastname))
year = input("[+] How years old?: ")
print("Entered {} years old".format(year))
country = input("[+] Where you from?: ")
print("Entered {} country".format(country))
occupation = input("[+] What is your occupation?: ")
print("Entered {} occupation".format(occupation))

student = Student("Lucho", "Suares", 32, "Uruguay", "professional football player")
student.presentation()

student.name = name
student.lastname = lastname
student.year = year
student.country = country
student.occupation = occupation
student.presentation()
