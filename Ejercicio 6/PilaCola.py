import numpy as np
class PilaCola:
    __items: np.array
    __top: int #cantidad de elementos en la pila
    __prim: int
    __ult: int
    __cantidad: int #max
    
    def __init__(self,dimension):
        self.__items = np.empty(dimension,dtype=int)
        self.__top = 0
        self.__prim = 0
        self.__ult = 0
        self.__cantidad = dimension
    
    def Vacia(self):
        return self.__top == 0

    def insertar(self,item):
        if self.__top < self.__cantidad:
            self.__items[self.__ult] = item
            self.__ult = (self.__ult+1)%self.__cantidad
            self.__top += 1
        else:
            print("Pila llena")
        
    def suprimir(self):
        if not self.Vacia():
            np.delete(self.__items,self.__prim)
            self.__prim = (self.__prim + 1)%self.__cantidad #elimina el primer elemento de la pila
            self.__top -= 1 
        else:
            print("Pila vacia")
    
    def recorrer(self):
        aux = self.__prim
        for i in range(self.__top):
            print(self.__items[aux])
            aux += 1

if __name__ == "__main__":
    PilaCola = PilaCola(4)
    PilaCola.insertar(1)
    PilaCola.insertar(2)
    PilaCola.insertar(3)
    PilaCola.insertar(4)
    PilaCola.suprimir()
    PilaCola.recorrer()