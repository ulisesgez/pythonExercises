#lista de mascotas
mascotas = ["perro", "gato", "canario", "hamster", "pez"]
#acceder a un elemento de la lista:
print(mascotas[0])
#cambar un elemento de la lista:
mascotas[0] =  "conejo"
print(mascotas[0])#imprime conejo
print(mascotas[0:2])#imprime conejo y gato
print(mascotas[-1])#imprime pez
print(mascotas[::2])#imprime conejo, canario y pez
print(mascotas[::-1])#imprime pez, hamster, canario, gato y conejo
print(mascotas[1::2])#imprime gato y hamster

numeros = list(range(21))
print(numeros[::2])#imprime los numeros pares
print(numeros[1::2])#imprime los numeros impares
#Del ejemplo anterior podemos hacerlo de otra forma:
numeros = list(range(1, 21))
print(numeros[::2])#imprime los numeros impares