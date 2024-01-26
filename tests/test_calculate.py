import pytest

from src.item import Item

@pytest.mark.calculate
class TestCalculate:
    """Тесты проверяющие корректность общей денежной суммы товаров
    """    
    
    def test_calculate(self, items):
        """Проверка денежной суммы исходя из количества товаров

        Args:
            items (fixture): инициализация трех элементов
        """        
        
        assert items[2].calculate_total_price() == 9.0
        assert items[1].calculate_total_price() == 4.0
        assert items[0].calculate_total_price() == 1.0
        
    def test_zero_calcutale(self, init_item):
        """Проверка вывода при нулевом значении

        Args:
            init_item (fixture): инициализация одного элемента
        """   
        
        init_item.quantity = 0
        assert init_item.calculate_total_price() == 0
               