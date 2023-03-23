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

#class is a blueprint for creating instances each employee will be instances of the employee class
emp_1 = Employee('Ami','Cabrera',50000)
emp_2 = Employee('Tomi','Cabrera',45000)
emp_3 = Employee('adel','Cabrera',60000)

print(Employee.nums_of_emps)
