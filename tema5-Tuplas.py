# Las tuplas son una especie de lista pero no es editable una vez definida
# Estas pueden almacenar objetos de diferentes tipos

tupla = (1,2,3)
print(tupla)
print(type(tupla))

tupla2 = (7, "Jonathan", True, 23.8, 16+7j)

print(tupla2)

# Se puede acceder a los objetos de una tupla a través de su indice
print(tupla2[1])

# Para acceder al ultimo objeto de una tupla se puede obtener de dos formas distintas
print(tupla2[4])
# o
print(tupla2[-1])

# Para obtener a un cierto rango de objetos de la tupla
print(tupla2[0:3])
print(tupla2[:3])
print(tupla2[3:])

# Se puede desintegrar la tupla en diferentes variables
a,b,c = tupla

print(a)
print(c)

# Tambien se puede concatenar el contenido de dos tuplas en una
tuplaN = tupla + tupla2
# Aqui devuelve el numero de apariciones del numero 2 en la tupla
tupla.count(2)