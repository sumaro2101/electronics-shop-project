import pytest

@pytest.mark.property
class TestPrice:
    
    def test_property_price(self, init_item):
        """Тест переназначения поля цена
            Дает новые своиста полю и проверяет корректность
        Args:
            init_item (fixture): инициализированный класс
        """
        
        init_item.price = 44.4
        assert init_item.price == 44.4
        
        
    def test_raise_price1(self, init_item):
        """Тест исключений поля цена
            Дает новые своиста полю и проверяет исключения
        Args:
            init_item (fixture): инициализированный класс
        """
        
        with pytest.raises(TypeError):
            init_item.price = "44.4"
            
            
    def test_raise_price2(self, init_item):
        """Тест исключений поля цена
            Дает новые своиста полю и проверяет исключения
        Args:
            init_item (fixture): инициализированный класс
        """
        
        with pytest.raises(ValueError):
            init_item.price = 0.0
            
        with pytest.raises(ValueError):
            init_item.price = -1.0
            