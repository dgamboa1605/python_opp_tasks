import unittest.mock
from io import StringIO

from unittest.mock import patch
from tasks.ex11_final_project.map import Map
from tasks.ex11_final_project.map_square import MapSquare
from tasks.ex11_final_project.player import Player
from tasks.ex11_final_project.items.pokeball import Pokeball
from tasks.ex11_final_project.pokemon.pikachu import Pikachu
from tasks.ex11_final_project.pokemon.charmander import Charmander

player = Player(0)
player.backpack.new_item(Pokeball(amount=10))
player.backpack.add_pokemon(Pikachu())
map_squares = []
map_square1 = MapSquare(2)
map_square1.x_pos = 0
map_square1.y_pos = 0
map_squares.append(map_square1)
map_square2 = MapSquare(2)
map_square2.x_pos = 0
map_square2.y_pos = 1
map_squares.append(map_square2)
map_square3 = MapSquare(2)
map_square3.x_pos = 1
map_square3.y_pos = 0
map_squares.append(map_square3)
map_square4 = MapSquare(2)
map_square4.x_pos = 1
map_square4.y_pos = 1
map_squares.append(map_square4)


def test_get_player_position_true():
    map = Map(2, 2)
    map.map_squares = map_squares
    assert map.get_player_position(player) is True


def test_get_pokemon_of_player():
    map = Map(2, 2)
    with unittest.mock.patch('builtins.input', return_value='Pikachu'):
        pokemon = map.get_pokemon_of_player(player)
        assert pokemon.name == 'Pikachu'


def test_get_pokemon_attack():
    map = Map(2, 2)
    map.found_pokemon = Charmander()
    with unittest.mock.patch('builtins.input', return_value='thunder attack'):
        map.get_pokemon_attack(Pikachu())
        assert map.found_pokemon.health == 400


def test_catch_pokemon():
    map = Map(2, 2)
    map.found_pokemon = Charmander()
    with unittest.mock.patch('builtins.input', return_value='y'):
        map.xp_level = 1000
        map.catch_pokemon(player)

        assert len(player.backpack.items) == 3


def test_find_square():
    x_pos = 1
    y_pos = 1
    map = Map(2, 2)
    map.map_squares = map_squares
    square = map.find_square(x_pos, y_pos)

    assert square.type == 'G'


def test_get_player_pokemon():
    name = 'Pikachu'
    item = Map.get_player_pokemon(player, name)
    assert item.name == 'Pikachu'


def test_get_player_pokemon_without_pokemons():
    name = 'test'
    item = Map.get_player_pokemon(player, name)
    assert item is False


def test_get_pokemon():
    pokemon = Map.get_pokemon(2)
    assert pokemon.name == 'Charmander'


def test_draw():
    test = \
        'You are standing in x: 0 y: 0\n'\
        '_____________________ X = Player\n'\
        '│   │   │   │   │   │ T = Small Town\n'\
        '│___│___│___│___│___│ G = Grass\n'\
        '│   │   │ G │ G │   │ F = Forest\n'\
        '│___│___│___│___│___│ H = House\n'\
        '│   │   │ X │ G │   │ C = Cave\n'\
        '│___│___│___│___│___│ L = Lake\n'\
        '│   │   │   │   │   │\n'\
        '│___│___│___│___│___│\n'\
        '│   │   │   │   │   │\n'\
        '│___│___│___│___│___│\n'

    map = Map(2, 2)
    map.map_squares = map_squares
    with patch('sys.stdout', new=StringIO()) as fake_out:
        map.draw(player)
        assert fake_out.getvalue() == test
