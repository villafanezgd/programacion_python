#Leer A y B, enteros. Calcular C = A x B mediante sumas sucesivas e imprimir el
#resultado.

valor_A = int(input("Ingrese el valor de A:"))
valor_B = int(input("Ingrese el valor de B:"))

sumas_sucesivas = 0
contador = 0
while (valor_A != contador):
    contador = contador + 1
    sumas_sucesivas = sumas_sucesivas + valor_B

print("El valor de la multiplicacion de A con B es :" + str(sumas_sucesivas))