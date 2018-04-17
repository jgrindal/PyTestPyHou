import pytest


class cheese_db():
    def __init__(self, cheese_dict={}):
        if len(cheese_dict) is 0:
            self.cheese_dict = {'Brie': 'No.', 'Gouda': 'No', 'Camenbert': 'We do have some camenbert!'}
        else:
            self.cheese_dict = cheese_dict

    def num_cheeses(self):
        return len(self.cheese_dict)

    def do_you_have(self, index):
        return self.cheese_dict[index]


@pytest.fixture()
def base_cheese_db():
    return cheese_db()


@pytest.fixture()
def custom_cheese_db():
    a_dictionary_for_now = {'Camenbert': 'Its a bit runny.', 'Gouda': 'Afraid Not'}
    return cheese_db(cheese_dict=a_dictionary_for_now)


def test_cheese_database(base_cheese_db):
    assert base_cheese_db.num_cheeses() == 3


@pytest.mark.usefixtures('custom_cheese_db')
def test_brie():
    assert custom_cheese_db().do_you_have('Gouda') == 'Afraid Not'
