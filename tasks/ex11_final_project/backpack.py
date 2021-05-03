
class Backpack:

    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items

    def add_pokemon(self, pokemon):
        self.__items.append(pokemon)

    def __str__(self):
        backpack_str = 'Backpack: \n'
        for item in self.__items:
            backpack_str += str(item) + '\n'
        return backpack_str

    def get_item(self, identifier):
        for item in self.__items:
            if hasattr(item, 'identifier'):
                if item.identifier == identifier:
                    return item
        return False

    def set_item(self, identifier, amount):
        item = self.get_item(identifier)
        ind = self.__items.index(item)
        self.__items[ind].amount = amount
        if amount == 0:
            self.__items.pop(ind)

    def new_item(self, item):
        if self.get_item(item.identifier) is False:
            self.__items.append(item)
            return

        item = self.get_item(item.identifier)
        ind = self.__items.index(item)

        self.__items[ind].amount = item.amount
        if item.amount <= 0:
            self.__items.pop(ind)
