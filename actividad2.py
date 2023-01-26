class operaciones:
    """Se definen propiedades de clase"""
    n1 = 0
    n2 = 0
    res = 0
    """Despues se define el constructor"""
    def __init__(self, a, b):
        self.n1=a
        self.n2=b
    
    """Finalmente los metodos de la clase"""
    def suma(self):
        self.res=self.n1+self.n2

    def resta(self):
        self.res=self.n1-self.n2

    def multiplicacion(self):
        self.res=self.n1*self.n2
    
    def division(self):
        self.res=self.n1/self.n2

def main():
    i=5
    while i!=0:
        opcion = int(input("Escribe el numero de la operacion que quieres realizar"+
                            " \n 1.- Suma\n2.- Resta\n3.- Multiplicacion\n 4.- Division \n"))
        num1 = int(input("Escribe el primer numero \n"))
        num2 = int(input("Escribe el segundo numero \n"))
        obj=operaciones(num1, num2)

        if(opcion == 1):
            obj.suma()
            print("La suma es {}".format(obj.res))
        elif(opcion == 2):
            obj.resta()
            print("La resta es {}".format(obj.res))
        elif(opcion == 3):
            obj.multiplicacion()
            print("La multiplicacion es {}".format(obj.res))
        elif(opcion == 4):
            obj.division()
            print("La division es {}".format(obj.res))
        i = int(input("¿Deseas continuar? \n Escribe 1 para continuar o 0 para salir \n"))    

if __name__ == '__main__':
    main()