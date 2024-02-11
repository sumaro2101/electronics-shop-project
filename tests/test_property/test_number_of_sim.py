import pytest

@pytest.mark.property
class TestSim:
    def test_number_of_sim(self, init_phone):
        """Тест переназначения поля сим-карты

        Args:
            init_phone (fixture): инициализированный под-класс
        """        
            
        init_phone.number_of_sim = 3
        assert init_phone.number_of_sim == 3
        
    def test_number_of_sim_raises_float(self, init_phone):
        """Тест переназначения поля сим-карты

        Args:
            init_phone (fixture): инициализированный под-класс
        """        
        with pytest.raises(TypeError):    
            init_phone.number_of_sim = 3.2
    
        
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