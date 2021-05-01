from tasks.ex11_final_project.pokemon.pokemon import Pokemon


class Pikachu(Pokemon):

    def __init__(self, identifier=4, name='Pikachu', health=700, power=700):
        super().__init__(identifier, name, health, power)

    def thunder_attack(self, pokemon):
        health = pokemon.health - int((self.power % 2))
        pokemon.health = health
        return pokemon

    def __str__(self):
        return super().__str__()
