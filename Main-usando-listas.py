
'''
Dudas:
A- Claridad en el programa, como se escribe segun usos y costumbres?
B- Como hago para que no este todo en el mismo txt? se puede atomizar cada parte?

Inconvenientes:

1- buscarcliente() funciona si:
    a) el cliente estaba harcodeado en el programa
    b) busca un numero.
 si busca un string de un cliente que se cargo con crearcliente() no funciona

2- falta la parte de crear y buscar transacciones

3- cuando busca un buscarcliente corre, imprime None para los argumentos que no coinciden con la palabra
    buscada. (los otros 3 que no coincidan con Apellido, Nombre o CUIT)

'''

# .............Consulta de clientes/transacciones....................


def consultarcliente(consulta):
    # aca faltaria agregarle que chequee si existe
    consulta = clientList[consulta]
    print(
        "El cliente n°: %s \n %s, %s. \n CUIT: %s \n"
        % (consulta[0],
            consulta[1],
            consulta[2],
            consulta[3])
            )
    return


def consultartransaccion(consulta):
    print(
        "La transaccion n°: %s \n en la fecha: %s.\n Producto: %s. \n Importe total: %s \n"
        % (consulta[0],
        consulta[1],
        consulta[2],
        consulta[3])
             )
    return

# .............Creacion de clientes/transacciones....................


def crearcliente():
    print("Ahora se creara un nuevo cliente.")

    codigoNuevoCliente = len(clientList) + 1   # mostrar el numero de cliente creado
    apellido = input("Ingrese el apellido del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    CUIT = input("Ingrese la CUIT del cliente: ")
    clientList[codigoNuevoCliente] = [codigoNuevoCliente, apellido, nombre, CUIT]


    print("Se creo un nuevo cliente con: n°: %s \n %s, %s. \n CUIT: %s \n"
         % (codigoNuevoCliente,
        apellido,
        nombre,
        CUIT)
        )
    return


def creartransaccion():
    pass


# .............Borrar clientes/transacciones....................

def borrarclientes(cliente):
    print("Se borrara el cliente: \n")
    consultarcliente(cliente)
    respuesta = input("Esta seguro? [S para confirmar]: ")
    if respuesta == "s" or respuesta == "S":
        del clientList[cliente]
        print("Cliente borrado.")
    else:
        pass


# -------------------------
# clientes harcodeados

clientList = {
    1: [1, "Arocena", "Juan Manuel", "30-25125842-2"],
    2: [2, "Villar", "Sandra", "23-251152842-2"]
}

# -------------------------
# transacciones harcodeadas

transaccionList = {
    1: [1, "22 de marzo del 2015", "remera estampada", 4500.00],
    2: [2, "17 de abril del 2016", "taza ploteada", 1500.00]  # suponiendo que vendes un unico producto con
                                                              # un precio unico
}


# .......................BUSQUEDAS...........................

# BUSQUEDA POR NOMBRE


def buscarcliente(busqueda):
    print("Se buscara el cliente con: %s" % busqueda)
    ultimokey = sorted(clientList.keys())[-1]
    for key in range(1, ultimokey+1):
        for x in clientList[key]:
            if x == busqueda:
                print("Cliente encontrado: ")
                print(consultarcliente(key))
    # else:
    #      print("no se encontro")


        # return print("No se encontro el cliente")

# ----------------MAIN---------------------------------------

print(clientList)
borrarclientes(1)
print(clientList)
