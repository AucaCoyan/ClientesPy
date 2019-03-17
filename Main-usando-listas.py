
'''
Dudas:
A- Claridad en el programa, como se escribe segun usos y costumbres?
B- Como hago para que no este todo en el mismo txt? se puede atomizar cada parte?

Inconvenientes:

1- buscarcliente() funciona si:
    a) el cliente estaba harcodeado en el programa
    b) busca un string dentro del diccionario.
 si busca un string de un cliente que se cargo con crearcliente() no funciona

2- falta la parte de crear y buscar transacciones

'''

# -------------------------------------------------------------------------------
#                 INICIO DATOS EN EL CODIGO DEL PROGRAMA
# -------------------------------------------------------------------------------

# -------------------clientes harcodeados-------------------

clientList = { #inicio lista de clientes harcodeados
    1: {                    #incio cliente 1
        "Codigo": 1,
        "Apellido": "Arocena",
        "Nombre": "Juan Manuel",
        "CUIT": "30-25125842-2"
    },                      #fin cliente 1
    2: {                    #incio cliente 2
        "Codigo": 2,
        "Apellido": "Villar",
        "Nombre": "Sandra",
        "CUIT": "23-251152842-2"
    }                       #fin cliente 2
}               #fin lista de clientes harcodeados

# -------------------transacciones harcodeadas-------------------

# ahora son listas, modificar a diccionarios y que acepten mas de un item (o probar con un item primero)
transaccionList = {
    1: [1, "22 de marzo del 2015", "remera estampada", 4500.00],
    2: [2, "17 de abril del 2016", "taza ploteada", 1500.00]  # suponiendo que vendes un unico producto con
                                                              # un precio unico
}

# --------------------FIN DATOS EN EL CODIGO DEL PROGRAMA-----------------------

# -------------------------------------------------------------------------------
#                   COMIENZO DEL PROGRAMA
# -------------------------------------------------------------------------------

# .............Creacion de clientes/transacciones....................


def crearcliente():
    print("Ahora se creara un nuevo cliente.")

    codigoNuevoCliente = len(clientList) + 1   # mostrar el numero de cliente creado
    print(codigoNuevoCliente)
    apellidonuevo = input("Ingrese el apellido del cliente: ")
    nombrenuevo = input("Ingrese el nombre del cliente: ")
    CUITnuevo = input("Ingrese la CUIT del cliente: ")
    clientList[codigoNuevoCliente] = {
        "Codigo": codigoNuevoCliente,
        "Apellido": apellidonuevo,
        "Nombre": nombrenuevo,
        "CUIT": CUITnuevo
    }
    print("Se creo un nuevo cliente con: n°: %s \n %s, %s. \n CUIT: %s \n"
         % (codigoNuevoCliente,
        apellidonuevo,
        nombrenuevo,
        CUITnuevo)
        )
    return


def creartransaccion():
    pass


# .............Borrar clientes/transacciones....................

def borrarclientes(clienteaborrar):
    print("Se borrara el cliente: \n")
    consultarcliente(clienteaborrar)
    respuesta = input("Esta seguro? [S para confirmar]: ")
    if respuesta == "s" or respuesta == "S":
        del clientList[clienteaborrar]
        print("Cliente borrado.")
    else:
        pass


def borrartransaccion(transaccionaborrar):
    print("Se borrara la transaccion: \n")
    consultartransaccion(transaccionaborrar)
    respuesta = input("Esta seguro? [S para confirmar]: ")
    if respuesta == "s" or respuesta == "S":
        del transaccionList[transaccionaborrar]
        print("Transaccion borrada.")
    return

# .......................BUSQUEDAS...........................

def consultarcliente(codigocliente):                        # BUSQUEDA POR CODIGO
    try:                                                    # prueba si el cliente existe
        clienteaimprimir = clientList[codigocliente]
    except:                                                 # el cliente no existe
        print("No se pudo encontrar cliente")
    else:                                                   # el cliente existe y lo encontro
        print("El cliente n°: %s \n %s, %s. \n CUIT: %s \n"
        % (clienteaimprimir["Codigo"],
            clienteaimprimir["Apellido"],
            clienteaimprimir["Nombre"],
            clienteaimprimir["CUIT"])
            )
    return


def consultartransaccion(codigotransaccion):                # BUSQUEDA POR CODIGO
    print(
        "La transaccion n°: %s \n en la fecha: %s.\n Producto: %s. \n Importe total: %s \n"
        % (codigotransaccion[0], #esto no es mas una lista, (debe ser) un diccionario
        codigotransaccion[1],
        codigotransaccion[2],
        codigotransaccion[3])
             )
    return

def buscarcliente(palabrabusqueda):                         # BUSQUEDA POR NOMBRE
    print("Se buscara el cliente con: %s." % palabrabusqueda)
    ultimokey = sorted(clientList.keys())[-1]
    for key in range(1, ultimokey+1):
        for x in clientList[key]:
            if clientList[key][x] == palabrabusqueda:  # aca pregunta si es igual, hay que agregar si contiene a
                consultarcliente(key)
    # else:                                             # el objetivo es si no coincide apellido, nombre o cuit
    #     print("No se encontro el valor buscado.")     # en la realidad se fija si cuit coincide con palabrabuscada
    #                                                           y asi con los otros argumentos. entonces
    #                                                           siempe pasa que encuentra 1 pero falla en los
    #                                                           3 que no coinciden con la busqueda
    # return
# -------------------------------FIN FUNCIONES-----------------------------------

# -------------------------------------------------------------------------------
#                                    MAIN
# -------------------------------------------------------------------------------

consultarcliente(2)