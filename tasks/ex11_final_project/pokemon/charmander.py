from tasks.ex11_final_project.pokemon.pokemon import Pokemon


class Charmander(Pokemon):

    def __init__(self, identifier=2, name='Charmander', health=400, power=600):
        super().__init__(identifier, name, health, power)

    def flame_thrower(self, pokemon):
        health = pokemon.health - int((self.power % 2))
        pokemon.health = health
        return pokemon

    def __str__(self):
        return super().__str__()
