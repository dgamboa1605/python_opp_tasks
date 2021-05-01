from tasks.ex11_final_project.pokemon.pokemon import Pokemon


class Bulbasaour(Pokemon):

    def __init__(self, identifier=1, name='Bulbasaour', health=400, power=500):
        super().__init__(identifier, name, health, power)

    def razor_leaf(self, pokemon):
        health = pokemon.health - int((self.power % 2))
        pokemon.health = health
        return pokemon

    def __str__(self):
        return super().__str__()
