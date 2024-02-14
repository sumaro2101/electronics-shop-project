import pytest
from src.item import Item, InstantiateCSVError

@pytest.mark.csv
class TestCsv:
    def test_csv(self, init_item, csv_file):
        """Тест проверка добавления объектов в список all

        Args:
            init_item (fixture): инициализация одного элемента
            csv_file (fixture): путь к тестовому csv 
        """      
          
        Item.instantiate_from_csv(csv_file)
        for i in Item.all:
            print(i.name)
        assert len(Item.all) == 3
        
        
    def test_csv_value(self, init_item):
        """Проверка правильности записи объектов в список all

        Args:
            init_item (fixture): инициализация одного элемента
        """        

        assert Item.all[-1].name == 'dictionary'
        
        
    def test_raise_csv(self, init_item):
        """Тест не найденого файла

        Args:
            init_item (fixture): инициализация одного элемента
        """    
            
        with pytest.raises(FileNotFoundError):
            init_item.instantiate_from_csv('fs')
            
    def test_raise_csv_damage(self, init_item, error_csv_file):
        """Тест поврежденного файла

        Args:
            init_item (fixture): инициализация одного элемента
            error_csv_file (fixture): путь к заведомо поврежденному файлу
        """    
            
        with pytest.raises(InstantiateCSVError):
            init_item.instantiate_from_csv(error_csv_file)
            