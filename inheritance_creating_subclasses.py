
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

class Developer(Employee):
    raise_amount =1.10

    def __init__(self,first,last,pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay, Employee=None):
        super().__init__(first, last, pay)
        if Employee is None:
            self.Employee =[]
        else:
            self.Employee = Employee
    def add_emp(self, emp):
        if emp not in self.Employee:
            self.Employee.append(emp)
    def remove_emp(self, emp):
        if emp in self.Employee:
            self.Employee.remove(emp)
    def print_emps(self):
        for emp in self.Employee:
            print('-->', emp.fullname())


dev_1 = Developer('Ami','Cabrera',50000, "Python")
dev_2 = Developer('Adel','Cabrera',60000, "Java")

mgr_1 = Manager('Tyler', 'Durden', 90000,[dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

print(isinstance(mgr_1,Manager))#para ver si pertenece a una instancia de clase (instancia sospechosa,clase o subclase )
print(issubclass(Developer,Employee))#para ver si es una subclase (subclase sospechosa,clase )





#print(help(Developer)) PARA VER LA CADENA DE CLASES Y SUS FUNCIONES DENTRO



