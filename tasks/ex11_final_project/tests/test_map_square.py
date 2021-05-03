from tasks.ex11_final_project.map_square import MapSquare


def test_print_str():
    map_square = MapSquare(0)
    assert str(map_square.type) == ' '
    map_square = MapSquare(1)
    assert str(map_square.type) == 'T'
    map_square = MapSquare(2)
    assert str(map_square.type) == 'G'
    map_square = MapSquare(3)
    assert str(map_square.type) == 'F'
    map_square = MapSquare(4)
    assert str(map_square.type) == 'H'
    map_square = MapSquare(5)
    assert str(map_square.type) == 'C'
    map_square = MapSquare(6)
    assert str(map_square.type) == 'L'
