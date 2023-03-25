#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

numero=float(input("introduce un numero: "))
divisor = float(input("introduce el divisor: "))
if numero == 0:
    print("perra no puedo dividir por 0 , obviamente")
else:
    print(int(numero/divisor))


