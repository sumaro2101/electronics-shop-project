import pytest

@pytest.mark.repr
def test_repr(init_item):
    assert repr(init_item) == "Item('test', 55, 10)"
    
@pytest.mark.repr
def test_repr_phone(init_phone):
    assert repr(init_phone) == "Phone('Phone', 100, 5, 2)"