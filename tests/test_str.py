import pytest

@pytest.mark.str
def test_str(init_item):
    assert str(init_item) == "test"