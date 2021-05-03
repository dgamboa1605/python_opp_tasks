from tasks.ex11_final_project.player import Player


def test_go_to_west():
    player = Player(0)
    player.go_to('west')
    assert player.x == -1


def test_go_to_east():
    player = Player(0)
    player.go_to('east')
    assert player.x == 1


def test_go_to_south():
    player = Player(0)
    player.go_to('south')
    assert player.y == -1


def test_go_to_north():
    player = Player(0)
    player.go_to('north')
    assert player.y == 1
