from tasks.ex11_final_project.items.item import Item


class Banana(Item):

    def __init__(self, identifier=2, name='Banana', amount=0):
        super().__init__(identifier, name, amount)

    def __str__(self):
        return super().__str__()
