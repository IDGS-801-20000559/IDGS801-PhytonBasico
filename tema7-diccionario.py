# Un diccionario es similar a la lista. Almacenan en base a su indice y su valor
# Se definen usando las llaves {}
# Se almacena similar al formato json

miDiccionario = {"Matricula":112, "Nombre": "Dario", "Edad": 23}

print(type(miDiccionario))
print(miDiccionario)

# Se puede acceder al valor de un diccionario agregando como parametro el identificador
# En este caso, el identificador es Nombre y se modifica con Panfilo
miDiccionario["Nombre"] = "Panfilo"
print(miDiccionario)
print(miDiccionario["Edad"])
print(miDiccionario.values())
print(miDiccionario.keys())