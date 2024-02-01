import pytest

@pytest.mark.repr
def test_repr(init_item):
    assert repr(init_item) == "Item('test', 55, 10)"