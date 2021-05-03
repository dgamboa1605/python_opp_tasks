
class Item:

    def __init__(self, identifier, name, amount):
        self.__identifier = identifier
        self.__name = name
        self.__amount = amount

    @property
    def identifier(self):
        return self.__identifier

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, new_amount):
        self.__amount = new_amount

    def __str__(self):
        return self.name + ' amount: ' + str(self.amount)
