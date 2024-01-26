import pytest

from src.item import Item

@pytest.fixture(scope='class')
def init_item():
    item = Item("test", 55.5, 10)
    return item

@pytest.fixture(scope='class')
def items():
    item1 = Item("test1", 1.0, 1)
    item2 = Item("test2", 2.0, 2)
    item3 = Item("test3", 3.0, 3)
    return item1, item2, item3