class Parametr:
    """Дексриптор данных
    """    
    
    @classmethod
    def __verify_param(cls, name: str, param) -> None:
        """Верификация данных поступаемых в параметры класса

        Args:
            name (str): имя поля
            param (any): значение поспающее в поле
            
            _name проверяет строку
            _price проверят цисло и дробь а так же значение меньше нуля
            _quantity проверят цисло и значение меньше нуля
        """        
        
        if name == "__name":
            if not isinstance(param, str):
                raise TypeError("Параметр 'Имя' ожидал строку")
            
        if name == "__price":
            if not isinstance(param, int|float):
                raise TypeError("Параметр 'Цена' ожидал цисло с плавающей точкой или целое число")
            if param <= 0.0:
                raise ValueError("Параметр 'Цена' не может быть ноль или меньше нуля")
            
        if name == "__quantity":
            if not isinstance(param, int):
                raise TypeError("Параметр 'Количество' ожидал цисло")
            if param < 0:
                raise ValueError("Параметр 'Количество' не может быть меньше нуля")
    
    
    def __set_name__(self, owner, name: str) -> None:
        """Модифицирует имя поля для инкапсуляции
        """        
        self.name = "__" + name
        
        
    def __get__(self, instance, owner) -> (str|float|int):
        """Получения значения из поля
        """   
             
        return getattr(instance, self.name)
    
    
    def __set__(self, instance, value) -> None:
        """Назначение значения в поле
        """    
            
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
        
     
    @classmethod
    def __validate_discount(cls, cof: int|float):
        if not isinstance(cof, int|float):
            raise TypeError(f"Скидка: Ожидалось число или дробь, не {type(cof)}")
        
        if cof < 0:
            raise ValueError("Скидка: Ожидалось значение больше нуля")
        
        
    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        __summary_price = self.price * self.quantity
        return __summary_price
    

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        
        self.__validate_discount(self.pay_rate)
        self.price *= self.pay_rate
    