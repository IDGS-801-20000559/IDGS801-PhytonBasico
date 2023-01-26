class OpenBas:
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


def main():
    obj=OpenBas(3,2)
    obj.suma()
    print("La suma es {}".format(obj.res))

if __name__ == '__main__':
    main()