import pytest

@pytest.mark.property
class TestItemProperty:
    """Тесты параметров класса
    """    

    def test_property_name(self, init_item):
        """Тест переназначения поля имя
            Дает новые своиста полю и проверяет корректность
        Args:
            init_item (fixture): инициализированный класс
        """
              
        init_item.name = "full_test"
        assert init_item.name == "full_test"
        
    
    def test_raise_name(self, init_item):
        """Тест исключений поля имя
            Дает новые своиста полю и проверяет исключения
        Args:
            init_item (fixture): инициализированный класс
        """
        
        with pytest.raises(TypeError):
            init_item.name = 423
       
            
    def test_len_name(self, init_item):
        """Тест на корректировку имени если оно больше чем 10 символов

        Args:
            init_item (fixture): инициализированный класс
        """  
              
        init_item.name = "myfirstnameisnone"
        assert init_item.name == "myfirstnam"
            
        
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
            init_item.quantity = 20.0
        
        with pytest.raises(TypeError):
            init_item.quantity = "20.0"
            
            
    def test_raise_quantity2(self, init_item):
        """Тест исключений поля количество
            Дает новые своиста полю и проверяет исключения
        Args:
            init_item (fixture): инициализированный класс
        """
        
        with pytest.raises(ValueError):
            init_item.quantity = -1
            
            
    def test_number_of_sim(self, init_phone):
        """Тест переназначения поля сим-карты

        Args:
            init_phone (fixture): инициализированный под-класс
        """        
            
        init_phone.number_of_sim = 3
        assert init_phone.number_of_sim == 3
        
        
    def test_number_of_sim_raises_zero(self, init_phone):
        """Тест искючения поля если параметр ноль

        Args:
            init_phone (fixture): инициализированный под-класс
        """  
              
        with pytest.raises(ValueError):
            init_phone.number_of_sim = 0
    
    
    def test_number_of_sim_raises_negative_digit(self, init_phone):
        """Тест искючения поля если параметр отрицательный

        Args:
            init_phone (fixture): инициализированный под-класс
        """  
        
        with pytest.raises(ValueError):
            init_phone.number_of_sim = -1
    
    
    def test_raise_nubmer_of_sim_init(self, init_phone):
        """Тест исключения в случае назначения не прильного значения
        
        Args:
            init_phone (fixture): инициализированный под-класс
        """   
             
        with pytest.raises(TypeError):
            init_phone.number_of_sim = "2"
            
            
    def test_result(self, init_item):
        assert init_item.name == "myfirstnam"
        assert init_item.price == 44.4
        assert init_item.quantity == 0
    