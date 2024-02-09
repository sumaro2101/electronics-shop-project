from .item import Item, Parametr

class Phone(Item):
    
    
    number_of_sim = Parametr()
    
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = self.string_to_number(number_of_sim)
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"