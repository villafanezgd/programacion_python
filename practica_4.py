#Dada una serie de números enteros, determinar el valor máximo, mínimo y las
#posiciones en que éstos se encontraban en la serie. El programa deberá ir
#preguntando si hay más números para ingresar.

valor_maximo = valor_minimo = int(input("Ingrese valor: "))
posicion_valor_maximo = posicion_valor_minimo = contador = 1
respuesta = input("¿Desea seguir ingresando valores? (SI/NO): ")

while (respuesta == "SI"):
    valor = int(input("Ingrese valor: "))
    contador = contador + 1
    if(valor > valor_maximo):
        valor_maximo = valor
        posicion_valor_maximo = contador

    if(valor < valor_minimo):
        valor_minimo = valor
        posicion_valor_minimo = contador

    respuesta = input("¿Desea seguir ingresando valores? (SI/NO): ")

print("El valor maximo es " + str(valor_maximo) + " y estaba en la posicion " + str(posicion_valor_maximo))
print("El valor minimo es " + str(valor_minimo) + " y estaba en la posicion " + str(posicion_valor_minimo))