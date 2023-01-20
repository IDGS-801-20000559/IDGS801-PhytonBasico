tablas = [1,2,3,4,5,6,7,8,9,10]

valor = int(input("Dame un numero y te doy su tabla \n"))

for val in tablas:
    print("{} por {} = {}".format(valor, val, (valor * val)))