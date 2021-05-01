MAP_OPTIONS = {
    0: ' ',
    1: 'T',
    2: 'G',
    3: 'F',
    4: 'H',
    5: 'C',
    6: 'L'
}

RANDOM_PHRASES = ['i am not quite sure what you mean by {0}',
                  'are you crazy! I can not do {0}',
                  'i do not know how to say this but.. {0} does not mean anything',
                  'Talking gibberish is a sign of impending mental collapse',
                  'That does not make any sense',
                  'next time, try to say something useful',
                  'I do not agree']


def print_description():
    print('             _                                 _  \n' +
          '            | |                               | | \n' +
          ' _ __   ___ | | _____ _ __ ___   ___  _ __    | | \n' +
          '|  _ \ / _ \| |/ / _ \  _   _ \ / _ \|  _ \   |_| \n' +
          '| |_) | (_) |   <  __/ | | | | | (_) | | | |   _  \n' +
          '|  __/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|  (_) \n' +
          '| |                                               \n' +
          '|_|                                               \n')

    print('Hello there! Welcome to the world of pokemon!\n' +
          'This world is inhabited by creatures called pokemon!\n' +
          'For some people, pokemon are pets. Others use them for fights.\n\n' +
          'At the moment there are not any pokemon in the around\n' +
          'You can use help for help \n')


def print_help():
    print('map                      :View Map\n'
          'west,east,south,north    :Move around the map\n'
          'catch                    :Catch pokemon (have to be standing in tall grass (G) in the map)\n'
          'backpack                 :Inventory\n'
          'exit                     :Exit game\n'
          'help                     :What do you think?\n')


def print_possible_attacks():
    print('Pikachu      :thunder attack\n'
          'Bulbasaour   :razor leaf\n'
          'Charmander   :flame thrower\n'
          'Pidgeotto    :quick attack\n'
          'Pikachu      :thunder attack\n'
          'Zubat        :air cutter')
