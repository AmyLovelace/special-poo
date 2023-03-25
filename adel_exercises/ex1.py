#Ciclo para imprimir todos los numeros primos 1 a 100

# is_greater = 18 > 0
# print(is_greater)

# is_odd =((8 % 3) > 0) or ((6 % 3) == 0)
# print(is_odd)

# is_true_1 = True or True #True
# is_true_2 = True or False #True
# is_true_3 = False or True #True
# is_true_4 = False or False #False
# is_true_5 = True and True #True
# is_true_6 = False and True #False
# is_true_7 = True and False #False
# is_true_8 = False and False #False


# print(is_true_1)
# print(is_true_2)
# print(is_true_3)
# print(is_true_4)
# print(is_true_5)
# print(is_true_6)
# print(is_true_7)
# print(is_true_8)

def prime_number ( max_number ):
    
    for number in range(2, max_number + 1):
        if number % 3 == 0 and number % 2 ==0: 
            pass
        elif number % 3 == 0:
            pass
        elif number > 2 and number % 2 == 0:
            pass
        elif number > 5 and number % 5 == 0:
            pass
        else:
            print(number)

prime_number(100)
