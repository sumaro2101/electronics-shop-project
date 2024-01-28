import pytest
from src.item import Item

@pytest.mark.csv
class TestCsv:
    def test_csv(init_item, csv_file):
        """Тест проверка добавления объектов в список all

        Args:
            init_item (fixture): инициализация одного элемента
            csv_file (fixture): путь к тестовому csv 
        """      
          
        Item.instantiate_from_csv(csv_file)
        for i in Item.all:
            print(i.name)
        assert len(Item.all) == 3
        
        
    def test_csv_value(init_item):
        """Проверка правильности записи объектов в список all

        Args:
            init_item (fixture): инициализация одного элемента
        """        

        assert Item.all[-1].name == 'dictionary'    