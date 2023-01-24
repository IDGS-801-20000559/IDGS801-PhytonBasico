def tem():
    print("Hola desde my_modulo.py")


def tem2():
    print("Adios desde my_modulo.py")

def main():
    print("Hola desde main")
    tem()
    tem2()

"""Es similar al main en java. Se ejecuta unicamente al correr el mismo codigo"""
if __name__ == '__main__':
    main()