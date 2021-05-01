MAP_OPTIONS = {
    0: ' ',
    1: 'T',
    2: 'G',
    3: 'F',
    4: 'H',
    5: 'C',
    6: 'L'
}

random_phrases = ['wtf does {0} mean?',
                  'i am not quite sure what you mean by {0}',
                  'are you crazy! I can not do {0}',
                  'i do not know how to say this but.. {0} does not mean anything',
                  'Talking gibberish is a sign of impending mental collapse',
                  'That does not make any sense',
                  'next time, try to say something useful',
                  'No!',
                  'I do not agree']


def print_description():
    print('You are in some fancy adventure fantasy place\n' +
          'there are not any Pókemon in the around\n' +
          'use help for help \n\n')


def print_help():
    print('map                          :View Map\n'
          'west,east,south,north        :Move around the map\n'
          'catch                        :Catch pokemon (have to be standing in tall grass)\n'
          'inv                          :Inventory\n'
          'exit                         :Exit game\n'
          'help                         :What do you think?\n')
