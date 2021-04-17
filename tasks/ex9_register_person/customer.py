from tasks.ex9_register_person.person import Person


class Customer(Person):

    def __init__(self, name, last_name, age, gender, email, phone_number):
        super().__init__(name, last_name, age, gender, email, phone_number)

    def __str__(self) -> str:
        return str("Name: " + self.name + "\n" +
                   "Last Name: " + self.last_name + "\n" +
                   "Age: " + self.age + "\n" +
                   "Gender: " + self.gender + "\n" +
                   "Email: " + self.email + "\n" +
                   "Phone Number: " + self.phone_number + "\n")
