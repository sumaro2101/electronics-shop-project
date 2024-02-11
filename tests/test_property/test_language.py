import pytest


@pytest.mark.property    
class TestLen:
    """Тесты параметра language
    """
    def test_language(self, init_keyboard):
        """Тест изменения языка

        Args:
            init_keyboard (fixture): инициалзированный класс
        """    
            
        init_keyboard.change_lang()
        assert init_keyboard.language == 'RU'
        
        
    def test_language_raise(self, init_keyboard):
        """Тест на исключения при попытке поменять значение в ручную

        Args:
            init_keyboard (fixture): инициалзированный класс
        """  
              
        with pytest.raises(AttributeError):
            init_keyboard.language = 'RU'
            