class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

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

    @classmethod
    def __validate_name(cls, name):
        if not isinstance(name, str):
            raise TypeError("Параметр 'Имя' ожидал строку")
        
    @classmethod
    def __validate_price(cls, price):
        if not isinstance(price, float):
            raise TypeError("Параметр 'Цена' ожидал цисло с плавающей точкой")
        if price <= 0.0:
            raise ValueError("Параметр 'Цена' не может быть ноль или меньше нуля")
        
    @classmethod
    def __validate_quantity(cls, quantity):
        if not isinstance(quantity, int):
            raise TypeError("Параметр 'Количество' ожидал цисло")
        if quantity < 0:
            raise ValueError("Параметр 'Количество' не может быть меньше нуля")
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__validate_name(name)
        self.__name = name
        
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__validate_price(price)
        self.__price = price
        
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity):
        self.__validate_quantity(quantity)
        self.__quantity = quantity
        
    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        pass

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        pass