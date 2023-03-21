class employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+last +'@company.com' 
    def fullname(self):
        return '{} {}'.format(self.first, self.last)  
    
#class is a blueprint for creating instances each employee will be instances of the employee class
emp_1 = employee('Ami','Cabrera',50000)
emp_2 = employee('Tomi','Cabrera',45000)
print(emp_1.email)
print(emp_2.email)

print(employee.fullname(emp_1))


