from bitacora import Bitacora

bitacora = Bitacora()

def get_sicks(people):
    result = 0
    for person in people:
        if person.is_sick:
            if person not in bitacora.people_sick:
                bitacora.add_sick_person(person)
            result += 1
    return result


def get_recover(people):
    result = 0
    for person in people:
        if not person.is_sick and person in bitacora.people_sick:
            bitacora.add_recovered_person(person)
            bitacora.remove_sick_person(person)
            result += 1
    return result

def get_women_sick():
    count = 0
    for i in bitacora.people_sick:
        if i.gender == "Female":
            count +=1
    return count

def get_man_sick():
    count = 0
    for i in bitacora.people_sick:
        if i.gender == "Male":
            count +=1
    return count

def get_women_recovered():
    count = 0
    for i in bitacora.people_recovered:
        if i.gender == "Female":
            count +=1
    return count

def get_man_recovered():
    count = 0
    for i in bitacora.people_recovered:
        if i.gender == "Male":
            count +=1
    return count

def get_adult_sick():
    count = 0
    for i in bitacora.people_sick:
        if i.age >= 35 and i.age <= 65:
            count +=1
    return count

def get_young_sick():
    count = 0
    for i in bitacora.people_sick:
        if i.age >= 18 and i.age <= 34:
            count +=1
    return count

def get_kid_sick():
    count = 0
    for i in bitacora.people_sick:
        if i.age >= 0 and i.age <= 17:
            count +=1
    return count

def get_adult_recovered():
    count = 0
    for i in bitacora.people_recovered:
        if i.age >= 35 and i.age <= 65:
            count +=1
    return count

def get_young_recovered():
    count = 0
    for i in bitacora.people_recovered:
        if i.age >= 18 and i.age <= 34:
            count +=1
    return count

def get_kid_recovered():
    count = 0
    for i in bitacora.people_recovered:
        if i.age >= 0 and i.age <= 17:
            count +=1
    return count