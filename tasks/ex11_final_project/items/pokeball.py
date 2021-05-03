from tasks.ex11_final_project.items.item import Item


class Pokeball(Item):

    def __init__(self, identifier=1, name='Pokeball', amount=0):
        super().__init__(identifier, name, amount)

    def __str__(self):
        return super().__str__()
