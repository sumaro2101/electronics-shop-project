from src.item import Item

class Keyboard(Item):
    
    
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.language = 'EN'
        
        
    @property
    def language(self):
        return self.__language
        