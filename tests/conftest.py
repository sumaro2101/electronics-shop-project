import pytest

from src.item import Item

@pytest.fixture()
def init_item():
    item = Item("test", 55.5, 10)
    return item