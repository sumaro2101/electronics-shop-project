import pytest
from csv import DictWriter
from src.item import Item
from src.phone import Phone

@pytest.fixture(scope='class')
def init_item():
    item = Item("test", "55.5", "10")
    return item

@pytest.fixture(scope='class')
def init_phone():
    phone = Phone("Phone", "100", "5", "2")
    return phone

@pytest.fixture(scope='class')
def items():
    Item.all = []
    item1 = Item("test1", "1.0", "1")
    item2 = Item("test2", "2.0", "2")
    item3 = Item("test3", "3.0", "3")
    return item1, item2, item3


@pytest.fixture(scope='function')
def csv_file(tmpdir_factory):
    file_to_csv = [{
        'name': 'myrandom',
        'price': 100,
        'quantity': 1
        },
        {
        'name':'linestock',
        'price':1000,
        'quantity':3,
        },
        {
        'name':'dictionary',
        'price':10,
        'quantity':5
        }
        ]
    temp_file = tmpdir_factory.mktemp("data").join("test_csv")
    print(temp_file)
    with temp_file.open('t+w') as f:
        file_csv = DictWriter(f, ('name', 'price', 'quantity'))
        file_csv.writeheader()
        file_csv.writerows(file_to_csv)
        
    return temp_file
