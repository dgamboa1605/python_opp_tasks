import random
import argparse

from tasks.ex11_final_project.pokemon.pikachu import Pikachu
from tasks.ex11_final_project.utils import print_description, print_help, RANDOM_PHRASES
from tasks.ex11_final_project.player import Player
from tasks.ex11_final_project.map import Map
from tasks.ex11_final_project.items.pokeball import Pokeball
from tasks.ex11_final_project.items.banana import Banana


def main(player_id, map_dimension, pokeball, banana):
    print_description()
    player = Player(player_id)
    map = Map(map_dimension, map_dimension)

    pikachu = Pikachu()

    player.backpack.new_item(Pokeball(amount=pokeball))
    player.backpack.new_item(Banana(amount=banana))
    player.backpack.add_pokemon(pikachu)

    while True:
        text_value = input('> ')
        if text_value == 'exit':
            print('Bye')
            break
        elif text_value == 'backpack':
            print(player.backpack)
        elif text_value == 'help':
            print_help()
        elif text_value == 'west' or text_value == 'east' or text_value == 'south' or text_value == 'north':
            player.go_to(text_value)
            map.draw(player)
        elif text_value == 'catch':
            if map.get_player_position(player):
                pokemon = map.get_pokemon_of_player(player)
                map.get_pokemon_attack(pokemon)
                map.catch_pokemon(player)
        elif text_value == 'map':
            map.draw(player)
        else:
            print(RANDOM_PHRASES[random.randint(0, 8)].format(text_value))


if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument('--player-id', required=True, help='player id to start the game', type=int)
    arg.add_argument('--map-dimension', required=True, help='map dimension e.g. 10 and map will be 10X10', type=int)
    arg.add_argument('--pokeball', default=10, help='amount of pokeball', type=int)
    arg.add_argument('--banana', default=10, help='amount of banana', type=int)

    args = arg.parse_args()

    main(player_id=args.player_id, map_dimension=args.map_dimension, pokeball=args.pokeball, banana=args.banana)
