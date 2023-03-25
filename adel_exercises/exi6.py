#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def mayoredad():
    edad = int(input("¿cual es tu edad?\n"))
    if edad < 18:
        print("eres menor de edad")
    else:
        print("eres mayor de edad")


mayoredad()
        