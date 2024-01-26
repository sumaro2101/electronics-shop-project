class Parametr:
    
    @classmethod
    def __verify_param(cls, name: str, param) -> None:
        
        if name == "_name":
            if not isinstance(param, str):
                raise TypeError("Параметр 'Имя' ожидал строку")
            
        if name == "_price":
            if not isinstance(param, float):
                raise TypeError("Параметр 'Цена' ожидал цисло с плавающей точкой")
            if param <= 0.0:
                raise ValueError("Параметр 'Цена' не может быть ноль или меньше нуля")
            
        if name == "_quantity":
            if not isinstance(param, int):
                raise TypeError("Параметр 'Количество' ожидал цисло")
            if param < 0:
                raise ValueError("Параметр 'Количество' не может быть меньше нуля")
    
    def __set_name__(self, owner, name: str) -> None:
        self.name = "_" + name
        
    def __get__(self, instance, owner) -> (str|float|int):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value) -> None:
        self.__verify_param(self.name, value)
        setattr(instance, self.name, value)
            
            

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    
    name = Parametr()
    price = Parametr()
    quantity = Parametr()


    def __new__(cls, *args, **kwargs):
        cls.all.append(super().__new__(cls))
        return cls.all[-1]
    
        
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
                
        self.name = name
        self.price = price
        self.quantity = quantity
     
        
    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        __summary_price = self._price * self._quantity
        return __summary_price
    

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        pass
    