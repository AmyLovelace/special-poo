#los metodos regulares automaticamente toman la primera instancia como argumento por convencion le nombramos SELF
#para que tome una clase como su argumento utilizare metodos de clase (class method)
class Employee:
    nums_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+last +'@company.com' 
        Employee.nums_of_emps+= 1
    
#las instancias de variables pueden ser unicas como los nombres emails la variable de la clase debe ser la misma para cada instancia

    def fullname(self):
        return '{} {}'.format(self.first, self.last)  
    
    def apply_raise(self):
        self.pay =int(self.pay * self.raise_amount)

    @classmethod #esto nos ayuda tomar la clase como el argument(self a cls(class))
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls,emp_str):#aqui utilizando el emp_str para separar la str gracias al .split de esta manera no vamos a poner cada instancia eb la funcion
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday()== 5 or day.weekday()== 6 :
            return False
        return True
        

#class is a blueprint for creating instances each employee will be instances of the employee class
emp_1 = Employee('Ami','Cabrera',50000)
emp_2 = Employee('Tomi','Cabrera',45000)
emp_3 = Employee('adel','Cabrera',60000)

import datetime
my_date = datetime.date(2023, 3, 23)
print(Employee.is_workday(my_date))
