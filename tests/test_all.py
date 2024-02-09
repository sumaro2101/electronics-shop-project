import pytest

from src.item import Item

@pytest.mark.all
class TestAll:
    """Тесты поля класса all с экземплярами класса
    """
    
    def test_all_count(self, items):
        """Тест количества сохраненых экземпляров

        Args:
            items (fixture): инициализация трех элементов
        """     
        
        assert len(Item.all) == 3    
        
    
    def test_check_name_in_all(self, items):
        """Тест ссылки на экземпляр класса

        Args:
            items (fixture): инициализация трех элементов
        """        
        
        assert items[0].name == Item.all[0].name
        assert items[1].name == Item.all[1].name
        assert items[2].name == Item.all[2].name
        
        
    def test_check_price_in_all(self, items):
        """Тест ссылки на экземпляр класса

        Args:
            items (fixture): инициализация трех элементов
        """        
        
        assert items[0].price == Item.all[0].price
        assert items[1].price == Item.all[1].price
        assert items[2].price == Item.all[2].price
        
        
    def test_check_quantity_in_all(self, items):
        """Тест ссылки на экземпляр класса

        Args:
            items (fixture): инициализация трех элементов
        """        
        
        assert items[0].quantity == Item.all[0].quantity
        assert items[1].quantity == Item.all[1].quantity
        assert items[2].quantity == Item.all[2].quantity
        
        
    @pytest.mark.xfail
    def test_duck_check_in_all1(self, items):
        assert items[0].name == items.name[1]
        
    @pytest.mark.xfail
    def test_duck_check_in_all2(self, items):    
        assert items[1].price == items.price[0]
        
    @pytest.mark.xfail
    def test_duck_check_in_all3(self, items):
        assert items[2].quantity == items.quantity[1]