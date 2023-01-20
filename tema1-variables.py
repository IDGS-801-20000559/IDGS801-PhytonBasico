# En python no es necesario definen tipos de datos

numero1 = "23";
numero2 = "24"

# Valor entero
a = 123
# Valores flotantes
b = 23.5
# Cadenas
c = "Roberto"

'''
Comentario de mas de una linea
Es linea de codigo que el lenguaje 
no interpreta
'''
# Conversion estricta de datos
print(numero1+numero2)

'''
Para parsear un tipo de dato se usan los metodos:
int()
float()
str()
'''
# Convierte la cadena en texto para poder
# realizar la operación
print(int(numero1)+int(numero2))

# En un valor flotante, solo toma el valor sin decimal
print(int(b))

# La función len() permite calcular la longitud de una cadena
valor = "123"
print(len(valor))

valor2 = 123
print(len(str(valor2)))