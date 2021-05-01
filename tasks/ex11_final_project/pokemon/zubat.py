from tasks.ex11_final_project.pokemon.pokemon import Pokemon


class Zubat(Pokemon):

    def __init__(self, identifier=5, name='Zubat', health=450, power=450):
        super().__init__(identifier, name, health, power)

    def air_cutter(self, pokemon):
        health = pokemon.health - int((self.power % 2))
        pokemon.health = health
        return pokemon

    def __str__(self):
        return super().__str__()

