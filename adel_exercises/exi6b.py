#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

import sys

def mayoredad():
    try:
        edad = int(sys.argv[1])
        if edad < 18:
            print("eres menor de edad")
        else:
            print("eres mayor de edad")
    except:
        print("mijita,argumento no es integer")
    


   
mayoredad()



        