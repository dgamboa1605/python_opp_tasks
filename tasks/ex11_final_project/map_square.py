from tasks.ex11_final_project.utils import MAP_OPTIONS


class MapSquare:

    def __init__(self, option_id):
        self.option_id = option_id
        self.type = MAP_OPTIONS.get(self.option_id)
        self.x_pos = None
        self.y_pos = None

    def __str__(self):
        return self.type
