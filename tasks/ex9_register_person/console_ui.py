from tasks.ex9_register_person.register_person import RegisterPerson
from tasks.ex9_register_person.customer import Customer
from tasks.ex9_register_person.manager import Manager
from tasks.ex9_register_person.banker import Banker
from tasks.ex9_register_person.credit_advisor import CreditAdvisor
from tasks.ex9_register_person.systems_administrator import SystemsAdministrator
from tasks.ex9_register_person.login import Login

register = RegisterPerson()

lines = "******************************************"


def get_attributes():
    print("\n****Register Employee****\n")
    name = input("Name: ")
    last_name = input("Last Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    email = input("Email: ")
    phone_number = input("Phone Number: ")
    salary = input("Salary: ")

    return name, last_name, age, gender, email, phone_number, salary


def sub_menu_options(opt):
    if opt == '1':
        try:
            name, last_name, age, gender, email, phone_number, salary = get_attributes()
            manager = Manager(name, last_name, age, gender, email, phone_number, salary)
            register.register_employee(manager)
        except ValueError as error:
            print("\n{}\n".format(error))

    if opt == '2':
        try:
            name, last_name, age, gender, email, phone_number, salary = get_attributes()
            banker = Banker(name, last_name, age, gender, email, phone_number, salary)
            register.register_employee(banker)
        except ValueError as error:
            print("\n{}\n".format(error))

    if opt == '3':
        try:
            name, last_name, age, gender, email, phone_number, salary = get_attributes()
            credit_advisor = CreditAdvisor(name, last_name, age, gender, email, phone_number, salary)
            register.register_employee(credit_advisor)
        except ValueError as error:
            print("\n{}\n".format(error))

    if opt == '4':
        try:
            name, last_name, age, gender, email, phone_number, salary = get_attributes()
            systems_administrator = SystemsAdministrator(name, last_name, age, gender, email, phone_number, salary)
            register.register_employee(systems_administrator)
        except ValueError as error:
            print("\n{}\n".format(error))


def sub_menu():
    run = True
    while run:
        print(lines)
        print("1. Register a Manager")
        print("2. Register a Banker")
        print("3. Register a Credit Advisor")
        print("4. Register a Systems Administrators")
        print("5. Back to Menu")
        print(lines)
        opt = input("Select an option: ")
        if opt == '5':
            run = False
        else:
            sub_menu_options(opt)


def menu_options(opt):
    if opt == '1':
        print("\n****Register Customer****\n")
        try:
            name = input("Name: ")
            last_name = input("Last Name: ")
            age = input("Age: ")
            gender = input("Gender: ")
            email = input("Email: ")
            phone_number = input("Phone Number: ")
            customer = Customer(name, last_name, age, gender, email, phone_number)
            register.register_customer(customer)
        except ValueError as error:
            print("\n{}\n".format(error))

    if opt == '2':
        sub_menu()

    if opt == '3':
        print(register.print_customer())

    if opt == '4':
        print(register.print_employee())


def menu():
    run = True
    while run:
        print(lines)
        print("1. Register a Customer")
        print("2. Register a Employee")
        print("3. Get Customers")
        print("4. Get Employees")
        print("5. Exit")
        print(lines)
        opt = input("Select an option: ")
        if opt == '5':
            run = False
        else:
            menu_options(opt)


def login():
    print("\n**Welcome to Go-Bank**\n")
    login = Login("admin", "admin")
    user = input("Enter your User: ")
    password = input("Enter your Password: ")

    if login.check(user, password):
        menu()


login()
