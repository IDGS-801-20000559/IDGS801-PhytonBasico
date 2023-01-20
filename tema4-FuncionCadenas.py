
cadena = "Universidad tecnologica de leon"

print(cadena)

# Modifica el texto a minuscula
print(cadena.lower())
# Modifica el texto a mayuscula
print(cadena.upper())
# Modifica el texto con estilo de titulo 
# Es decir, solo la primera en mayuscula
print(cadena.title())
# Muestra el indice de la palabra o letra.
print(cadena.find("de"))
# Te muestra cuantas a existe en la cadena
print(cadena.count("a"))
# Reemplaza las letras a por un numero 4
textoFinal = cadena.replace("a", "4")
print(textoFinal)

# La funcion split separa en un arreglo cada palabra
cadenaNueva = cadena.split(" ")
print(cadenaNueva)