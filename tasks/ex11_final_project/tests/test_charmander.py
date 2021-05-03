from tasks.ex11_final_project.pokemon.charmander import Charmander
from tasks.ex11_final_project.pokemon.pikachu import Pikachu

pikachu = Pikachu(health=500, power=500)


def test_flame_thrower_attack():
    charmander = Charmander(health=500, power=500)
    pokemon = charmander.flame_thrower(pikachu)
    assert pokemon.health == 500


def test_print_str():
    res = 'Charmander hp: 500 att: 500'
    charmander = Charmander(health=500, power=500)
    assert str(charmander) == res
