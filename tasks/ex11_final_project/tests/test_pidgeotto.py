from tasks.ex11_final_project.pokemon.pidgeotto import Pidgeotto
from tasks.ex11_final_project.pokemon.pikachu import Pikachu

pikachu = Pikachu(health=500, power=500)


def test_quick_attack():
    pidgeotto = Pidgeotto(health=500, power=500)
    pokemon = pidgeotto.quick_attack(pikachu)
    assert pokemon.health == 500


def test_print_str():
    res = 'Pidgeotto hp: 500 att: 500'
    pidgeotto = Pidgeotto(health=500, power=500)
    assert str(pidgeotto) == res
