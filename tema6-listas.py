# Las listas son arreglos pero también admite diferentes tipos de datos

nombres = ["Juan", "Mario", "Laura"]
numeros = [1,2,3,4,5]
datos = [1, 2.5, "Mario", True]

# A diferencia de las tuplas, las listas si se pueden modificar
nombres[0]="Mayami"

# Son diferentes formas de recorrer la lista
print(nombres[:])
print(nombres[2])
print(nombres[:3])
print(nombres[1:])

# De esta manera se agregan elementos a la lista
nombres.append("Gilberta")
print(nombres)
# Así reemplaza un objeto con respecto al indice
nombres.insert(2, "Llorona")
print(nombres)

# Agrega un conjunto de valores
nombres.extend(["chencha", 23.5, 34]) 
print(nombres)

# Elimina un cierto valor 
nombres.remove("chencha")
print(nombres)

# Elimina el ultimo valor en la lista
nombres.pop()
print(nombres)

n=["Juan"]
# Multiplica el contenido la lista n por 5
n2 = n*5
print(n2)

print(nombres)
del nombres[0]
print(nombres)