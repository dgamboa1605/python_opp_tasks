from tasks.ex11_final_project.items.banana import Banana


def test_print_str():
    res = 'Banana amount: 10'
    banana = Banana(amount=10)
    assert str(banana) == res
