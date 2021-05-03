from tasks.ex11_final_project.items.item import Item


def test_print_str():
    res = 'test amount: 20'
    item = Item(1, 'test', 20)
    assert str(item) == res
