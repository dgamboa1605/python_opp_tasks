from tasks.ex11_final_project.pokemon.bulbasaur import Bulbasaour
from tasks.ex11_final_project.pokemon.pikachu import Pikachu

pikachu = Pikachu(health=500, power=500)


def test_razor_leaf_attack():
    bulbasaour = Bulbasaour(health=500, power=500)
    pokemon = bulbasaour.razor_leaf(pikachu)
    assert pokemon.health == 500


def test_print_str():
    res = 'Bulbasaour hp: 500 att: 500'
    bulbasaour = Bulbasaour(health=500, power=500)
    assert str(bulbasaour) == res
