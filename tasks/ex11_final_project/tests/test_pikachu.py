from tasks.ex11_final_project.pokemon.pidgeotto import Pidgeotto
from tasks.ex11_final_project.pokemon.pikachu import Pikachu

pidgeotto = Pidgeotto(health=500, power=500)


def test_thunder_attack():
    pikachu = Pikachu(health=500, power=500)
    pokemon = pikachu.thunder_attack(pidgeotto)
    assert pokemon.health == 500


def test_print_str():
    res = 'Pikachu hp: 500 att: 500'
    pikachu = Pikachu(health=500, power=500)
    assert str(pikachu) == res
