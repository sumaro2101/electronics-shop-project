from csv import DictReader
from math import floor
from typing import Any

class Parametr:
    """Дексриптор данных
    """    
    
    @classmethod
    def __verify_name(cls, param: Any) -> None| str:
        """Верификация данных поступаемых в параметры класса

        Args:
            param (any): значение поступающее в поле
            
            __name проверяет стороку"""
            
        if not isinstance(param, str):
            raise TypeError("Параметр name должен быть строкой")
        
        if  len(param) > 10:
            correct_name = "".join(param[:10])
            return correct_name 
    
        return param
            
            
    @classmethod
    def __verify_price(cls, value: Any):
        """Верификация данных поступаемых в параметры класса

        Args:
            param (any): значение поступающее в поле
            
            __price проверят цисло и дробь а так же значение меньше нуля"""
            
        if not isinstance(value, int|float):
                raise TypeError("Параметр 'Цена' ожидал цисло с плавающей точкой или целое число")
        if value <= 0.0:
                raise ValueError("Параметр 'Цена' не может быть ноль или меньше нуля")
    
    
    @classmethod
    def __verify_quantity(cls, value: Any):
        """Верификация данных поступаемых в параметры класса

        Args:
            param (any): значение поступающее в поле
            
            __quantity проверят цисло и значение меньше нуля"""
            
        if not isinstance(value, int):
            raise TypeError("Параметр 'Количество' ожидал цисло")
        if value < 0:
            raise ValueError("Параметр 'Количество' не может быть меньше нуля")
    
        
    def __set_name__(self, owner, name: str) -> None:
        """Модифицирует имя поля для инкапсуляции
        """        
        self.name = "__" + name
        
        
    def __get__(self, instance, owner) -> Any:
        """Получения значения из поля
        """   
             
        return getattr(instance, self.name)
    
    
    def __set__(self, instance, value) -> None:
        """Назначение значения в поле
        """    
        if self.name == "__name":
            result = self.__verify_name(value)
            setattr(instance, self.name, result)
            
        if self.name == "__price":
            self.__verify_price(value)
            setattr(instance, self.name, value)
            
        if self.name == "__quantity":
            self.__verify_quantity(value)
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
        self.price = self.string_to_number(price)
        self.quantity = self.string_to_number(quantity)
        
    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
            
    @classmethod
    def __validate_discount(cls, cof: int|float):
        if not isinstance(cof, int|float):
            raise TypeError(f"Скидка: Ожидалось число или дробь, не {type(cof)}")
        
        if cof < 0:
            raise ValueError("Скидка: Ожидалось значение больше нуля")
        
        
    @classmethod
    def instantiate_from_csv(cls, csv):
        with open(csv, 'r+t') as f:
            file = DictReader(f)
            cls.all = []
            [(cls(item['name'], item['price'], item['quantity'])) for item in file]
        
        
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

    def __str__(self) -> str:
        return f"{self.name}"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
