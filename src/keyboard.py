from src.item import Item, Parametr
from typing import Any

class Parametr_lan(Parametr):
    @classmethod
    def _verify_name(cls, param: Any) -> None| str:
        """Верификация данных поступаемых в параметры класса

        Args:
            param (any): значение поступающее в поле
            
            __name проверяет стороку"""
            
        if not isinstance(param, str):
            raise TypeError("Параметр name должен быть строкой") 
        return param


class MixineLanguage:
    
    language_name = ('EN', 'RU')
    _language = 'EN'
    
    def change_lang(self):
        self._language = self.language_name[-1] if self._language == 'EN' else self.language_name[0]
            
    @property
    def language(self):
        return self._language


class Keyboard(Item, MixineLanguage):
    
    __slots__ = ('_language')
    name = Parametr_lan()
    
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self._language = 'EN'

    def change_lang(self):
        return super().change_lang()