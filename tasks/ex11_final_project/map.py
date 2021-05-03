import random

from tasks.ex11_final_project.map_square import MapSquare
from tasks.ex11_final_project.pokemon.zubat import Zubat
from tasks.ex11_final_project.pokemon.pidgeotto import Pidgeotto
from tasks.ex11_final_project.pokemon.bulbasaur import Bulbasaour
from tasks.ex11_final_project.pokemon.charmander import Charmander
from tasks.ex11_final_project.pokemon.pokemon import Pokemon
from tasks.ex11_final_project.utils import print_possible_attacks


class Map:
    def __init__(self, x_size, y_size):
        self.__x_size = x_size
        self.__y_size = y_size
        self.found_pokemon = None
        self.xp_level = None
        self.__map_squares = []
        self.__draw_map = [MapSquare(0), MapSquare(0), MapSquare(0), MapSquare(0), MapSquare(0), MapSquare(0),
                           MapSquare(0), MapSquare(0), MapSquare(0), MapSquare(0), MapSquare(0), MapSquare(0),
                           MapSquare(0), MapSquare(0), MapSquare(0), MapSquare(0), MapSquare(0), MapSquare(0),
                           MapSquare(0), MapSquare(0), MapSquare(0), MapSquare(0), MapSquare(1), MapSquare(2),
                           MapSquare(2), MapSquare(3), MapSquare(3), MapSquare(3), MapSquare(3), MapSquare(4),
                           MapSquare(4), MapSquare(5), MapSquare(6), MapSquare(6), MapSquare(6)]

        for x in range(0, self.__x_size):
            for y in range(0, self.__y_size):
                self.__map_squares.append(MapSquare(self.__draw_map[random.randint(0, 34)].option_id))
                self.__map_squares[-1].x_pos = x
                self.__map_squares[-1].y_pos = y

    @property
    def draw_map(self):
        return self.__draw_map

    @property
    def map_squares(self):
        return self.__map_squares

    @map_squares.setter
    def map_squares(self, new_map_squares):
        self.__map_squares = new_map_squares

    def get_player_position(self, player):
        if self.find_square(player.x, player.y).type == "G":
            return True
        else:
            print('Where do you see a pokemon?')
            return False

    def get_pokemon_of_player(self, player):
        self.found_pokemon = Map.get_pokemon(random.randint(1, 4))
        print('{} with health: {} power: {} is in sight'.format(self.found_pokemon.name, self.found_pokemon.health,
                                                                self.found_pokemon.power))
        print('what pokemon do you want to use to battle?')
        while True:
            pokemon_name = input('> ')
            pokemon = Map.get_player_pokemon(player, pokemon_name)
            if pokemon_name == 'help':
                print(player.backpack)
            elif pokemon is False:
                print('you do not have this pokemon, please select a correct pokemon')
            else:
                print(
                    'you selected {} with health: {} power: {} for battle'.format(pokemon.name, pokemon.health,
                                                                                  pokemon.power))
                break
        return pokemon

    def get_pokemon_attack(self, pokemon):
        while True:
            print('What attack do you want to use for {}?'.format(pokemon.name))
            pokemon_attack = input('> ')
            pokemon_attacks = [i.replace('_', ' ') for i in dir(pokemon) if not i.startswith('__')]
            if pokemon_attack == 'help':
                print_possible_attacks()
            elif pokemon_attack in pokemon_attacks:
                print('damage inflicted: {}'.format(str(int(pokemon.power / 2))))
                method = getattr(pokemon, pokemon_attack.replace(' ', '_'))
                self.found_pokemon = method(self.found_pokemon)
                self.xp_level = self.found_pokemon.health * self.found_pokemon.power
                print('{} with health: {}'.format(self.found_pokemon.name, self.found_pokemon.health))
                break
            else:
                print('{} does not have this attack'.format(pokemon.name))

    def catch_pokemon(self, player):
        while True:
            print('do you want to throw a pokeball? (y/n) def: y')
            if input() != 'n':
                if player.backpack.get_item(1):
                    player.backpack.set_item(1, player.backpack.get_item(1).amount - 1)
                    success = random.randint(0, self.xp_level)
                    if success < 200000:
                        player.backpack.add_pokemon(self.found_pokemon)
                        print('Yea you get the pokemon!!\n')
                        break
                    else:
                        print('{} does not want to enter the pokeball'.format(self.found_pokemon.name))
                else:
                    print('You do not have any pokeballs')
                    break
            else:
                print('Why did not you catch the pokemon? Well, maybe next time.')
                break

    def find_square(self, x, y):
        for square in self.__map_squares:
            if x == square.x_pos and y == square.y_pos:
                return square
        return MapSquare(0)

    @staticmethod
    def get_player_pokemon(player, name):
        items = player.backpack.items
        for item in items:
            if item.name == name:
                return item
        return False

    @staticmethod
    def get_pokemon(pokemon_id) -> Pokemon:
        pokemon = {
            1: Bulbasaour(),
            2: Charmander(),
            3: Pidgeotto(),
            4: Zubat()
        }
        return pokemon.get(pokemon_id)

    def draw(self, player):
        print('You are standing in x: ' + str(player.x) + ' y: ' + str(player.y))
        print('_____________________' + ' X = Player')
        print('│ {0} │ {1} │ {2} │ {3} │ {4} │'.format(self.find_square(player.x - 2, player.y + 2),
                                                       self.find_square(player.x - 1, player.y + 2),
                                                       self.find_square(player.x, player.y + 2),
                                                       self.find_square(player.x + 1, player.y + 2),
                                                       self.find_square(player.x + 2,
                                                                        player.y + 2)) + ' T = Small Town')
        print('│___│___│___│___│___│' + ' G = Grass')
        print('│ {0} │ {1} │ {2} │ {3} │ {4} │'.format(self.find_square(player.x - 2, player.y + 1),
                                                       self.find_square(player.x - 1, player.y + 1),
                                                       self.find_square(player.x, player.y + 1),
                                                       self.find_square(player.x + 1, player.y + 1),
                                                       self.find_square(player.x + 2, player.y + 1)) + ' F = Forest')
        print('│___│___│___│___│___│' + ' H = House')
        print('│ {0} │ {1} │ {2} │ {3} │ {4} │'.format(self.find_square(player.x - 2, player.y),
                                                       self.find_square(player.x - 1, player.y), 'X',
                                                       self.find_square(player.x + 1, player.y),
                                                       self.find_square(player.x + 2, player.y)) + ' C = Cave')
        print('│___│___│___│___│___│' + ' L = Lake')
        print('│ {0} │ {1} │ {2} │ {3} │ {4} │'.format(self.find_square(player.x - 2, player.y - 1),
                                                       self.find_square(player.x - 1, player.y - 1),
                                                       self.find_square(player.x, player.y - 1),
                                                       self.find_square(player.x + 1, player.y - 1),
                                                       self.find_square(player.x + 2, player.y - 1)))
        print('│___│___│___│___│___│')
        print('│ {0} │ {1} │ {2} │ {3} │ {4} │'.format(self.find_square(player.x - 2, player.y - 2),
                                                       self.find_square(player.x - 1, player.y - 2),
                                                       self.find_square(player.x, player.y - 2),
                                                       self.find_square(player.x + 1, player.y - 2),
                                                       self.find_square(player.x + 2, player.y - 2)))
        print('│___│___│___│___│___│')
