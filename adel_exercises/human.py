from random import choice
from string import ascii_lowercase, digits
from animal import Animal 

class Human(Animal,Walker):

    # Quiero que mi clase User tenga los siguientes attr:
    # nombre
    # edad
    # contraseña

    # Es nuestro constructor de instancias de nuestra clase
    # Atributos de clase
    # self hace referencia a la instancia

    def __init__(self, name='', age=0, password = None):
        self.name = name
        self.__age = age
        self.password = password
        Human.soul = True
        super().__init__()
        #super().__init__(type='Human',kingdom='hominidos')
    
    @classmethod 
    def status(cls,val):
        cls.soul = val

    def get_age(self):
        return self.__age 

    def set_password(self, pwd_length): # public method
        self.password = self.__generate_password(pwd_length)

    def __generate_password(self, pwd_length): # private method -> Encapsulamiento OOP
        letters_and_nums = ascii_lowercase + digits
        result_string = ''.join(choice(letters_and_nums) for i in range(pwd_length))
        return result_string

    def __str__(self):
        passwordIsNotNull = self.password if self.password else ''
        return f'{self.name} {self.__age} {passwordIsNotNull}'