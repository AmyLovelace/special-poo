
class Employee:

    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first +'.'+last +'@company.com' 
        self.pay = pay   
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)  
    
    def apply_raise(self):
        self.pay =int(self.pay * self.raise_amount)

dev_1 = Employee('Ami','Cabrera',50000)
dev_2 = Employee('Adel','Cabrera',60000)

print(dev_1.email)
print(dev_2.email)
