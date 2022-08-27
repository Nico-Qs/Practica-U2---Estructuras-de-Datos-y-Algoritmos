from PilaCoEncadenada import PilaCoEncadenada, Caja, Cliente


if __name__ == "__main__":
    
    tSimulacion = int(input('Ingrese el tiempo de la simulacion: '))
    tAtencionCajero = int(input('Ingrese el tiempo que el cajero atiende (en minutos): '))
    tFrecuenciaClientes = int(input('Ingrese la frecuencia de los clientes (en minutos): ')) 
    
    tTransc= 0
    tEsperaTotal = 0
    clientesTotales = 0
    clientesAtendidos = 0
    
    cola=PilaCoEncadenada()
    caja=Caja()
    while tTransc <= tSimulacion:
        tEsperaTotal += cola.getCantidad() # * tFrecuenciaClientes
        if tTransc % tFrecuenciaClientes == 0 and tTransc != 0:
            clientesTotales += 1
            cola.insertar(Cliente)
            print ("Llego el cliente N°: {}".format(clientesTotales))
        if  tTransc % tAtencionCajero == 0 and not cola.Vacia():
            clientesAtendidos += 1
            print ("Cliente atendido N°: {}".format(clientesAtendidos))
            caja.atendiendoCliente(cola.suprimir())
        
        tTransc += 1
    print ("\nClientes totales: {}".format(clientesTotales))
    print("\nClientes atendidos: {}".format(clientesAtendidos))
    print("Tiempo de espera promedio: {:.2f} minutos".format(tEsperaTotal/clientesTotales))