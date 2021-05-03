from tasks.ex11_final_project.backpack import Backpack
from tasks.ex11_final_project.items.item import Item
from tasks.ex11_final_project.pokemon.pokemon import Pokemon

item = Item(identifier=1, name='test item', amount=10)
pokemon = Pokemon(identifier=2, name='test pokemon', health=200, power=200)


def test_add_pokemon():
    backpack = Backpack()
    backpack.add_pokemon(pokemon)
    assert len(backpack.items) == 1


def test_get_item():
    backpack = Backpack()
    backpack.new_item(item)
    new_item = backpack.get_item(identifier=1)
    assert new_item.identifier == 1


def test_get_item_false():
    backpack = Backpack()
    assert backpack.get_item(identifier=1) is False


def test_set_item():
    backpack = Backpack()
    backpack.new_item(item)
    backpack.set_item(1, 20)
    assert backpack.items[0].amount == 20


def test_set_item_amount_zero():
    backpack = Backpack()
    backpack.new_item(item)
    backpack.set_item(1, 0)
    assert len(backpack.items) == 0


def test_new_item():
    backpack = Backpack()
    backpack.new_item(item)
    assert len(backpack.items) == 1
