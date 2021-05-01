from tasks.ex11_final_project.backpack import Backpack


class Player:

    def __init__(self, identifier):
        self.__identifier = identifier
        self.x = 0
        self.y = 0
        self.backpack = Backpack(20)

    def go_to(self, move_to):
        if move_to == 'west':
            self.x -= 1
        if move_to == 'east':
            self.x += 1
        if move_to == 'south':
            self.y -= 1
        if move_to == 'north':
            self.y += 1

