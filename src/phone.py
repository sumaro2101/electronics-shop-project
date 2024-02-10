from .item import Item
from typing import Any

class Phone(Item):
    
    
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = self.string_to_number(number_of_sim)
        
    @classmethod
    def __verify_number_of_sim(cls, value: Any):
        """Верификация данных поступаемых в параметры класса

        Args:
            param (any): значение поступающее в поле
            
            __number_of_sim проверят цисло и значение меньше или равно нуля"""
            
        if not isinstance(value, int):
            raise TypeError('Параметр "Количество карт" ожидал число')
        if value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        
    @property
    def number_of_sim(self):
        return self.__number_of_sim
    
    
    @number_of_sim.setter
    def number_of_sim(self, number):
        self.__verify_number_of_sim(number)
        self.__number_of_sim = number
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
    