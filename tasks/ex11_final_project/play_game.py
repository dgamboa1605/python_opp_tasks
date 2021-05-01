import random

from tasks.ex11_final_project.pokemon.pikachu import Pikachu
from tasks.ex11_final_project.utils import print_description, print_help, random_phrases
from tasks.ex11_final_project.player import Player
from tasks.ex11_final_project.map import Map
from tasks.ex11_final_project.items.pokeball import Pokeball
from tasks.ex11_final_project.items.banana import Banana

print_description()
player = Player(0)
map = Map(10, 10)

pikachu = Pikachu(health=random.randint(0, 400) + 100, power=random.randint(0, 400) + 100)

player.backpack.new_item(Pokeball(amount=10))
player.backpack.new_item(Banana(amount=10))
player.backpack.add_pokemon(pikachu)

map.draw(player)

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
        map.catch_pokemon(player)
    elif text_value == 'map':
        map.draw(player)
    else:
        print(random_phrases[random.randint(0, 8)].format(text_value))
