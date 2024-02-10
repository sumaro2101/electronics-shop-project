import pytest

@pytest.mark.property
class TestQuantity:
    
    def test_property_quantity(self, init_item):
        """Тест переназначения поля количество
            Дает новые своиста полю и проверяет корректность
        Args:
            init_item (fixture): инициализированный класс
        """
        
        init_item.quantity = 20
        assert init_item.quantity == 20
        
        
    def test_property_quantity_zero(self, init_item):
        """Тест переназначения поля количество
            Дает новые своиста полю и проверяет корректность
        Args:
            init_item (fixture): инициализированный класс
        """
        
        init_item.quantity = 0
        assert init_item.quantity == 0
        
    
    def test_raise_quantity1(self, init_item):
        """Тест исключений поля количество
            Дает новые своиста полю и проверяет исключения
        Args:
            init_item (fixture): инициализированный класс
        """
        
        with pytest.raises(TypeError):
            init_item.quantity = [20.0]
            
            
    def test_raise_quantity2(self, init_item):
        """Тест исключений поля количество
            Дает новые своиста полю и проверяет исключения
        Args:
            init_item (fixture): инициализированный класс
        """
        
        with pytest.raises(ValueError):
            init_item.quantity = -1
                    
    def test_result(self, init_item):
        assert init_item.name == "test"
        assert init_item.price == 55
        assert init_item.quantity == 0
        