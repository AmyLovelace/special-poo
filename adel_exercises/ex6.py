#crea una funcion fibonacci que reciba como arg un numero maximo de numero fibonacci para imprimir por pantalla de 1 al numero maximo 
# 1 1 2 3 5 8 13 21 34 ...

def fibo(max_number):

    current_number = 0
    last_number = 1



    for number in range(1, max_number +1):
        current_number = number
        current_number += last_number
        last_number = current_number
        print(current_number)

fibo(10)


