#crea una funcion que reciba un parametro max_number que imprima por pantalla todos los numeros pares del 1 al max number 

def even_number (max_number):
    for number in range (1, max_number + 1):
        if number % 2 == 0 :
            print(number)

even_number(100)
