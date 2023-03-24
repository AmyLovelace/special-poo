#estos special methods ayudar a emular algunos bluid in methods y tambien es como se emplementan operator overloading.
class Employee:

    raise_amount = 1.04

    def __init__(self,first,last,pay):#__init__ special methods
        self.first = first
        self.last = last
        self.email = first +'.'+last +'@company.com' 
        self.pay = pay   
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)  
    
    def apply_raise(self):
        self.pay =int(self.pay * self.raise_amount)

    def __repr__(self):#representacion no ambigua del objeto ,para ser leida por devs
        pass

    #def__str__(self):#representacion leible del objeto,para ser leida por el usuario
        pass


emp_1 = Employee('Ami','Cabrera',50000)
emp_2 = Employee('Adel','Cabrera',60000)

print(1+2)
print('a'+'b')