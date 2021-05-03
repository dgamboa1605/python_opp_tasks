from tasks.ex11_final_project.items.pokeball import Pokeball


def test_print_str():
    res = 'Pokeball amount: 10'
    pokeball = Pokeball(amount=10)
    assert str(pokeball) == res
