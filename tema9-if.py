
print("Valores de usuario \n a sumar")

num1 = int(input("Dame un valor "))
num2 = int(input("Dame otro valor "))

if(num1 > num2):
    print("{} es mayor que {}".format(num1, num2))
else:
    print("{1} es mayor que {0}".format(num1, num2))