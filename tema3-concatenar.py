# Concatenaciones de cadenas

texto1 = "Hola"
texto2 = "Mundo!"
#Se puede concatenar dentro de una variable
textoFinal = texto1+" "+texto2

print(textoFinal)

# Se puede concatenar usando %s
print("El saludo es %s %s"% (texto1,texto2))

# Se puede concatenar usando las llaves y la funcion format
# dentro de las llaves se puede usar el indice de la cadena
cadena = "Saludar dos: {} {}".format(texto1,texto2)

print(cadena)
cadena2 = "Saludar tres {x}{y}".format(x=texto1, y=texto2)
print(cadena2)