import pytest

@pytest.mark.add
class TestAdd:
    """Тесты суммирования полей
    """    
    
    def test_add(self, init_item, init_phone):
        """Тест суммирования полей классов

        Args:
            init_item (fixture): инициализированный класс
            init_phone (fixture): инициализированный под-класс
        """    
            
        assert init_item + init_phone == 15
        
        
    def test_add_not_class(self, init_item):
        """Тест суммирования с операндом не являющимся классом

        Args:
            init_item (fixture): инициализированный класс
        """
              
        assert init_item + 10 is None 