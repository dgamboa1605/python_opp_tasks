from tasks.ex11_final_project.pokemon.pokemon import Pokemon


def test_print_str():
    res = 'TestPokemon hp: 500 att: 500'
    pokemon = Pokemon(identifier=1, name='TestPokemon', health=500, power=500)
    assert str(pokemon) == res
