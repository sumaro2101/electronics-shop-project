import pytest

from src.item import Item

@pytest.mark.discount
class TestDiscount:
    """Тесты скидки для товаров
    """ 
    
    def test_discount(self, items):
        """Проверка применения скидки

        Args:
            items (fixture): инициализация трех элементов
        """        
        
        Item.pay_rate = 0.5
        items[2].apply_discount()
        
        assert items[2].price == 1.5
        assert items[0].price == 1.0
        
        
    def test_raises_discount(self, items):
        """Проверка исключений поля скидки

        Args:
            items (fixture): инициализация трех элементов
        """        
        
        with pytest.raises(TypeError):
            Item.pay_rate = "1"
            items[0].apply_discount()
            
        with pytest.raises(ValueError):
            Item.pay_rate = -1.0
            items[0].apply_discount()