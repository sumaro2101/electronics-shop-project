import pytest

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
           
        assert init_item.price == 55.5
        
    
    def test_fixture_quantity(self, init_item):
        """Тестирует наличие поля количество

        Args:
            init_item (fixture): инициализированный тестовый класс
        """     
           
        assert init_item.quantity == 10
        
        