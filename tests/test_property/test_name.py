import pytest

@pytest.mark.property
class TestName:
    
    def test_property_name(self, init_item):
        """Тест переназначения поля имя
            Дает новые своиста полю и проверяет корректность
        Args:
            init_item (fixture): инициализированный класс
        """
              
        init_item.name = "full_test"
        assert init_item.name == "full_test"
        
    def test_property_name_keyboard(self, init_keyboard):
        """Тест переназначения поля имя в классе keyboard
            Дает новые своиста полю и проверяет корректность
        Args:
            init_keyboard (fixture): инициализированный класс
        """
        
        init_keyboard.name = 'longtestwithmoretenchar'
        assert init_keyboard.name == 'longtestwithmoretenchar'
    
    
    def test_raise_name(self, init_item):
        """Тест исключений поля имя
            Дает новые своиста полю и проверяет исключения
        Args:
            init_item (fixture): инициализированный класс
        """
        
        with pytest.raises(TypeError):
            init_item.name = 423
      
       
    def test_raise_name_keyboard(self, init_keyboard):
        """Тест исключений поля имя в классе keyboard
            Дает новые своиста полю и проверяет исключения
        Args:
            init_keyboard (fixture): инициализированный класс
        """
        
        with pytest.raises(TypeError):
            init_keyboard.name = ['raise']
      
            
    def test_len_name(self, init_item):
        """Тест на корректировку имени если оно больше чем 10 символов

        Args:
            init_item (fixture): инициализированный класс
        """  
              
        init_item.name = "myfirstnameisnone"
        assert init_item.name == "myfirstnam"
            