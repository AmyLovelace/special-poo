class Employee:


    def __init__(self,first,last):#__init__ special methods
        self.first = first
        self.last = last
    @property    
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)  
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)  
    
    @fullname.setter
    def fullname(self, name):
        first,last =name.split(' ')
        self.first=first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print('delete name')
        self.first =None
        self.last =None
        
emp_1 = Employee('Adel','Popin')

emp_1.fullname='inay popon'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
