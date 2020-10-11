#Escribir un algoritmo que indique si un número entero, ingresado por un usuario,
#es primo.
'''
    10 -> 10/10, 10/9, 10/8, 10/7, 10/6 .... 10/1
    10/10 = 0, 10/9 = 1, 10/8 = 2, 10/7 = 3, 10/6 = 4, 10/5 = 0, 10/4 = 2, 10/3 = 4, 10/2 = 0, 10/1 = 0
'''
contador = valor = int(input("Ingrese numero: "))
cantidad_divisiones = 0
while(contador != 0):
    if(valor%contador == 0):
        cantidad_divisiones = cantidad_divisiones + 1
    contador = contador - 1

if (cantidad_divisiones == 2):
    print("El numero ingresado es primo")
else:
    print("El numero ingresado no es primo")
