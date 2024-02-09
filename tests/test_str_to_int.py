import pytest

from src.item import Item

@pytest.mark.strint
class TestStringNumber:
    
    def test_str_to_int_number(self):
        """Тест возращата значение int если int
        """  
              
        assert Item.string_to_number(50) == 50
        
        
    def test_str_to_int(self):
        """Тест преобразование строки в цифру
        """   
            
        assert Item.string_to_number("44") == 44
        

    def test_str_to_int2(self):
        """Тест преобразование строки в цифру с округлением
        """  
              
        assert Item.string_to_number("44.5") == 44
        
        
    def test_raise_str_to_int1(self):
        """Тест исключения
        """  
              
        with pytest.raises(TypeError):
            assert Item.string_to_number([24, 432])
            
            
    def test_raise_str_to_int2(self):
        """Тест исключения
        """   
             
        with pytest.raises(ValueError):
            assert Item.string_to_number("test")