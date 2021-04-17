from code.ex7_pandemic import report_generator
from code.ex7_pandemic.person import Person


class PandemicControl(object):
    def __init__(self, city):
        self.__city = city
        self.__people = []

    @property
    def city(self):
        return self.__city

    @property
    def people(self):
        return self.__people

    @people.setter
    def people(self, new_value):
        self.__people = new_value

    def print_report(self):
        print(f"----------------------For the City: [{self.__city}]----------------------")
        sick_number = report_generator.get_sicks(people)
        recovered = report_generator.get_recover(people)
        women_sick = report_generator.get_women_sick()
        man_sick = report_generator.get_man_sick()
        women_recovered = report_generator.get_women_recovered()
        man_recovered = report_generator.get_man_recovered()
        adult_sick = report_generator.get_adult_sick()
        young_sick = report_generator.get_young_sick()
        kid_sick = report_generator.get_kid_sick()
        adult_recovered = report_generator.get_adult_recovered()
        young_recovered = report_generator.get_young_recovered()
        kid_recovered = report_generator.get_kid_recovered()

        print(f"The number of persons that are sick is [{sick_number}]")
        print(f"The number of persons that are recovered from the sickness is [{recovered}]")
        print(f"The number of Women that are sick is [{women_sick}]")
        print(f"The number of Man that are sick is [{man_sick}]")
        print(f"The number of Women that are recovered from the sickness is [{women_recovered}]")
        print(f"The number of Man that are recovered from the sickness is [{man_recovered}]")
        print(f"The number of adult that are sick is [{adult_sick}]")
        print(f"The number of young that are sick is [{young_sick}]")
        print(f"The number of kid that are sick is [{kid_sick}]")
        print(f"The number of adult that are recovered from the sickness is [{adult_recovered}]")
        print(f"The number of young that are recovered from the sickness is [{young_recovered}]")
        print(f"The number of kid that are recovered from the sickness is [{kid_recovered}]")

        print(self.__people)


person1 = Person("name1", "last_name1", 45, "Male")
person2 = Person("name2", "last_name2", 30, "Female")
person3 = Person("name3", "last_name3", 50, "Male")
person4 = Person("name4", "last_name4", 15, "Female")

person1.is_sick = True
person2.is_sick = True
person3.is_sick = True
person4.is_sick = True

people = [person1, person2, person3, person4]

p = PandemicControl("Cbba")
p.people = people
p.print_report()

p.people[0].is_sick = False
p.people[1].is_sick = False

p.print_report()
