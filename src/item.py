from csv import DictReader
from math import floor
class Parametr:
    """Дексриптор данных
    """    
    
    @classmethod
    def __verify_param(cls, name: str, param) -> None:
        """Верификация данных поступаемых в параметры класса

        Args:
            name (str): имя поля
            param (any): значение поспающее в поле
            
            _price проверят цисло и дробь а так же значение меньше нуля
            _quantity проверят цисло и значение меньше нуля
        """        
                
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
        self.price = self.string_to_number(price)
        self.quantity = self.string_to_number(quantity)
        
     
    @classmethod
    def __validate_discount(cls, cof: int|float):
        if not isinstance(cof, int|float):
            raise TypeError(f"Скидка: Ожидалось число или дробь, не {type(cof)}")
        
        if cof < 0:
            raise ValueError("Скидка: Ожидалось значение больше нуля")
    
    
    @classmethod
    def __validate_name(cls, name: str) -> (str):
        """Валидация данных на строку и длину меньше 10 символов

        Args:
            name (str): Получает данные для обработки

        Raises:
            TypeError: Если не строка возращает исключение

        Returns:
            str: Возращает обработанный объект в случае если длина больше 10
        """  
              
        if not isinstance(name, str):
            raise TypeError("Параметр name должен быть строкой")
        
        if  len(name) > 10:
            correct_name = "".join(name[:10])
            return correct_name 
        
        return name
        
        
    @classmethod
    def instantiate_from_csv(cls, csv):
        with open(csv, 'r+t') as f:
            file = DictReader(f)
            cls.all = []
            [(cls(item['name'], item['price'], item['quantity'])) for item in file]
        
        
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = self.__validate_name(name)


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
    
    @staticmethod
    def string_to_number(string: str):
        if isinstance(string, int):
            return string
        
        if not isinstance(string, str):
            raise TypeError("Функция ожидала строку")
        
        if not string.isdigit():
            try:
                float(string)
                return floor(float(string))
            
            except ValueError:
                "Функция ожидала цифру в виде строки"
        
        return int(string)
