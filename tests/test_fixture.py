import pytest
from csv import DictReader

@pytest.mark.fixture
class TestFixture:
    """Тестовый класс с серией проверок фикстуры
    """   
     
    def test_fixture_name(self, init_item):
        """ Тестирует наличие поля Имя

        Args:
            init_item (fixture): инициализированный тестовый класс
        """     
        assert init_item.name == "test"
    
    
    def test_fixture_price(self, init_item):
        """Тестирует наличие поля Цена

        Args:
            init_item (fixture): инициализированный тестовый класс
        """     
           
        assert init_item.price == 55
        
    
    def test_fixture_quantity(self, init_item):
        """Тестирует наличие поля количество

        Args:
            init_item (fixture): инициализированный тестовый класс
        """     
           
        assert init_item.quantity == 10
        
        
    def test_fixture_number_of_sim(self, init_phone):
        """Тестирует наличие поля количество сим карт

        Args:
            init_phone (fixture): инициализированный тестовый под-класс
        """     
        
        assert init_phone.number_of_sim == 2
        
    def test_fixture_language(self, init_keyboard):
        """Тестирует наличие поля количество сим карт

        Args:
            init_phone (fixture): инициализированный тестовый под-класс
        """     
        
        assert init_keyboard.language == 'EN'
        
        
    def test_fixture_csv(self, csv_file):
        with csv_file.open() as f:
            file = DictReader(f)
            assert list(file)[0]['name'] == 'myrandom'
        