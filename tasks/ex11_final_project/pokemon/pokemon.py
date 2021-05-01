
class Pokemon:

    def __init__(self, identifier, name, health, power):
        self.__identifier = identifier
        self.__name = name
        self.__health = health
        self.__power = power

    @property
    def health(self):
        return self.__health

    @property
    def power(self):
        return self.__power

    @property
    def name(self):
        return self.__name

    @health.setter
    def health(self, new_health):
        self.__health = new_health

    def __str__(self):
        return str(self.name) + ' hp: ' + str(self.health) + ' att: ' + str(self.power)
