from tasks.ex11_final_project.pokemon.pokemon import Pokemon


class Pidgeotto(Pokemon):

    def __init__(self, identifier=3, name='Pidgeotto', health=500, power=500):
        super().__init__(identifier, name, health, power)

    def quick_attack(self, pokemon):
        health = pokemon.health - int((self.power % 2))
        pokemon.health = health
        return pokemon

    def __str__(self):
        return super().__str__()
