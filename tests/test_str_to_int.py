import pytest

from src.item import Item

@pytest.mark.strint
class TestStringNumber:
    def test_str_to_int(init_item):
        """Тест преобразование строки в цифру

        Args:
            init_item (fixture): инициализированный класс
        """   
            
        assert Item.string_to_number("44") == 44
        

    def test_str_to_int2(init_item):
        """Тест преобразование строки в цифру с округлением

        Args:
            init_item (fixture): инициализированный класс
        """  
              
        assert Item.string_to_number("44.5") == 44
        
        
    def test_raise_str_to_int1(init_item):
        """Тест исключения

        Args:
            init_item (fixture): инициализированный класс
        """  
              
        with pytest.raises(TypeError):
            assert Item.string_to_number([24, 432])
            
            
    def test_raise_str_to_int2(init_item):
        """Тест исключения

        Args:
            init_item (_type_): _description_
        """   
             
        with pytest.raises(ValueError):
            assert Item.string_to_number("test")