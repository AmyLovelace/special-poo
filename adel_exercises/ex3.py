#crea una funcion que reciba un parametro max_number que imprima por pantalla todos los numeros impares del 1 al max number 

def odd_number (maxnumber):
    for number in range (1,maxnumber + 1):
        if number % 2 != 0  :
            print(number)

odd_number(100)

