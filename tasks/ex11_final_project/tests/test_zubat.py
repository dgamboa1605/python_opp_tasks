from tasks.ex11_final_project.pokemon.zubat import Zubat
from tasks.ex11_final_project.pokemon.pikachu import Pikachu

pikachu = Pikachu(health=500, power=500)


def test_air_cutter_attack():
    zubat = Zubat(health=500, power=500)
    pokemon = zubat.air_cutter(pikachu)
    assert pokemon.health == 500


def test_print_str():
    res = 'Zubat hp: 500 att: 500'
    zubat = Zubat(health=500, power=500)
    assert str(zubat) == res
