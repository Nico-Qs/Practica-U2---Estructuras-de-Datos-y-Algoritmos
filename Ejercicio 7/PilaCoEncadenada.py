from ClaseNodo import Nodo


class PilaCoEncadenada:
    __primero: Nodo
    __ultimo: Nodo
    __cantidad: int
    
    def __init__(self):
        self.__cantidad = 0
        self.__primero = None
        self.__ultimo = None
    
    def insertar(self,elemento):
        nuevaNodo = Nodo(elemento)
        if self.__ultimo == None:
            self.__primero = nuevaNodo
        else:
            self.__ultimo.setSiguiente(nuevaNodo)
        self.__ultimo = nuevaNodo
        self.__cantidad += 1

    def Vacia(self):
        return self.__primero == None
    
    def suprimir(self):
        if not self.Vacia():
            x = self.__primero
            aux = self.__primero
            self.__primero = self.__primero.getSiguiente()
            if self.__primero == None:
                self.__ultimo = None
            del aux
            self.__cantidad -= 1
            return x
        else:
            print("No hay personas en la cola")
    
    def getCantidad(self):
        return self.__cantidad
    
    def recorrer(self):
        aux=self.__primero
        while aux != None:
            print(aux.getDato())
            aux=aux.getSiguiente()

class Cliente:
    __tiempoespera:int

    def __init__(self):
        self.__tiempoespera=0
    
    def incrementarTiempo(self):
        self.__tiempoespera += 1
    
    def getTiempoEspera(self):
        return self.__tiempoespera

class Caja:
    __cliente: Cliente
    __ocupada: bool

    def __init__(self):
        self.__cliente = None
        self.__ocupada = False
    
    def atendiendoCliente(self,cliente):
        self.__cliente = cliente
        self.__ocupada = True

    def clienteAtendido(self):
        self.__ocupada = False
        self.__cliente = None
    
    def ocupada(self):
        return self.__ocupada