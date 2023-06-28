
'''
Dudas:
A- Como hago para que no este todo en el mismo txt? se puede atomizar cada parte?

'''

# -------------------------------------------------------------------------------
#                 INICIO DATOS EN EL CODIGO DEL PROGRAMA
# -------------------------------------------------------------------------------

# -------------------clientes harcodeados-------------------

clientList = {  # inicio lista de clientes harcodeados
    1: {                    # incio cliente 1
        "Codigo": 1,
        "Apellido": "Arocena",
        "Nombre": "Juan Manuel",
        "CUIT": "30-25125842-2"
    },                      # fin cliente 1
    2: {                    # incio cliente 2
        "Codigo": 2,
        "Apellido": "Villar",
        "Nombre": "Sandra",
        "CUIT": "23-251152842-2"
    }                       # fin cliente 2
}               # fin lista de clientes harcodeados

# -------------------productos harcodeados-------------------

productList = {
    1:  {
        "Codigo": 1,
        "Nombre": "Taza ploteada",
        "Precio": 150.00},
    2: {
        "Codigo": 2,
        "Nombre": "Remera estampada",
        "Precio": 300.00},
}


# -------------------transacciones harcodeadas-------------------

transaccionList = {
    1: {
        "Codigo de transf": 1,
        "Nro de Cliente": 1,       # todo: en un futuro tendria que buscar cliente por nombre
        "Product List":
            {
            1: {
                "Item": 1,
                "Codigo de producto": 2,
                "Cantidad": 3,

                },
            2: {
                "Item": 2,
                "Codigo de producto": 1,
                "Cantidad": 2,
                }
        }
    },
    2: {
        "Codigo de transf": 2,
        "Nro de Cliente": 1,  # todo: en un futuro tendria que buscar cliente por nombre
        "Product List":
            {
                1: {
                    "Item": 1,
                    "Codigo de producto": 1,
                    "Cantidad": 5,

                },
                2: {
                    "Item": 2,
                    "Codigo de producto": 1,
                    "Cantidad": 22,
                }
            }
    }
}

# --------------------FIN DATOS EN EL CODIGO DEL PROGRAMA-----------------------

# -------------------------------------------------------------------------------
#                   COMIENZO DEL PROGRAMA
# -------------------------------------------------------------------------------

# .............Creacion de clientes/transacciones....................


def crearcliente():
    print("Ahora se creara un nuevo cliente.")  # aviso de creacion

    codigoNuevoCliente = len(clientList) + 1   # busca el ultimo numero de cliente creado y le suma uno
    apellidonuevo = input("Ingrese el apellido del cliente: ")  # sucesion de imputs
    nombrenuevo = input("Ingrese el nombre del cliente: ")
    CUITnuevo = input("Ingrese la CUIT del cliente: ")
    clientList[codigoNuevoCliente] = {                          # creacion efectiva del cliente
        "Codigo": codigoNuevoCliente,
        "Apellido": apellidonuevo,
        "Nombre": nombrenuevo,
        "CUIT": CUITnuevo
    }
    print("Se creo un nuevo cliente con: n°: %s \n %s, %s. \n CUIT: %s \n"  # mostrar que creo el programa
         % (codigoNuevoCliente,                                             # impresion de datos
            apellidonuevo,
            nombrenuevo,
            CUITnuevo)
          )
    return


def crearproducto():
    pass


def creartransaccion():
    print("Ahora se creara una nueva transaccion.")  # aviso de creacion

    codigoNuevaTransac = len(transaccionList) + 1  # busca el ultimo numero de cliente creado y le suma uno
    codigoClienteTransac = int(input("Ingrese el CODIGO del cliente de la nueva transaccion: "))
    tryclienteexiste(codigoClienteTransac)          # prueba si el cliente existe
    codigoProductoTransac = int(input("Ingrese el CODIGO del producto a agregar a la transaccion: "))
    tryproductoexiste(codigoProductoTransac)        # prueba si el producto existe
    cantidadProductoTransac = int(input("Ingrese la CANTIDAD del producto a agregar a la transaccion: "))
    transaccionList[codigoNuevaTransac] = {         # creacion efectiva de la transaccion
        "Codigo de transf": codigoNuevaTransac,
        "Nro de Cliente": codigoClienteTransac,
        "Product List":{
            1: {
                "Item": 1,
                "Codigo de producto": codigoProductoTransac,
                "Cantidad": cantidadProductoTransac,
                }
        }
    }

#    productosaaagregar = {}  # fixme ojo que si agrega vacio queda vacio en el dict

    itemaagregar = 0
    while True:
        masproductos = input("Desea agregar mas productos: [S/N] ")
        if masproductos == "n" or masproductos == "N":
            break
        else:
            itemaagregar = itemaagregar + 1
            codigoProductoTransac = int(input("Ingrese el CODIGO del producto a agregar a la transaccion: "))
            tryproductoexiste(codigoProductoTransac)  # prueba si el producto existe
            cantidadProductoTransac = int(input("Ingrese la CANTIDAD del producto a agregar a la transaccion: "))
            transaccionList[codigoNuevaTransac]["Product List"] = {
                itemaagregar: {
                    "Item": itemaagregar,
                    "Codigo de producto": codigoProductoTransac,
                    "Cantidad": cantidadProductoTransac
                }
            }

    print("La transaccion ha sido creada.")
    return


# .............Borrar clientes/transacciones....................

def borrarclientes(clienteaborrar):
    print("Se borrara el cliente: \n")
    if consultarcliente(clienteaborrar) == False:
        return
    respuesta = input("Esta seguro? [S para confirmar]: ")
    if respuesta == "s" or respuesta == "S":
        del clientList[clienteaborrar]
        print("Cliente borrado.")
    else:
        print("El cliente no se borro.")
    return


def borrarproducto(productoaborrar):
    pass

def borrartransaccion(transaccionaborrar):
    print("Se borrara la transaccion: \n")
    consultartransaccion(transaccionaborrar)
    respuesta = input("Esta seguro? [S para confirmar]: ")
    if respuesta == "s" or respuesta == "S":
        del transaccionList[transaccionaborrar]
        print("Transaccion borrada.")
    else:
        print("La transaccion no se borro.")
    return

# .......................TRY EXISTE...........................


def tryclienteexiste(codigocliente):
    try:                                                    # prueba si el cliente existe
        clientList[codigocliente]
    except:                                                 # el cliente no existe
        print("No se pudo encontrar el cliente.")
        return False
    else:
        return True
    finally:
        print("se ejecutó la función")


def tryproductoexiste(codigoproducto):
    try:                                                    # prueba si el producto existe
        productList[codigoproducto]
    except:                                                 # el producto no existe
        print("No se pudo encontrar el producto.")
        return False
    else:
        return True


def trytransaccionexiste(codigotransaccion):
    try:                                                    # prueba si la transaccion existe
        transaccionList[codigotransaccion]
    except:                                                 # la transaccion no existe
        print("No se pudo encontrar la transaccion.")
        return False
    else:
        return True

# .......................BUSQUEDAS...........................


def consultarcliente(codigocliente):                        # BUSQUEDA POR CODIGO
    if tryclienteexiste(codigocliente) == False:
        return                                              # fixme: aca me gustaria que corte la funcion, que no
                                                            #    pregunte si estoy seguro si no encontro el cliente

    else:                                                   # El cliente existe y lo encontro
        clienteaimprimir = clientList[codigocliente]
        print("El cliente n°: %s \n %s, %s. \n CUIT: %s \n"
        % (clienteaimprimir["Codigo"],
            clienteaimprimir["Apellido"],
            clienteaimprimir["Nombre"],
            clienteaimprimir["CUIT"])
            )
    return


def consultartransaccion(codigotransaccion):                # BUSQUEDA POR CODIGO
    if trytransaccionexiste(codigotransaccion) == False:
        return                                              # fixme: idem consultarcliente
    print(
        "La transaccion n°: %s \n en la fecha: %s.\n Producto: %s. \n Importe total: %s \n"
        % (codigotransaccion[0],                            #  todo: esto no es mas una lista es un diccionario
        codigotransaccion[1],                               #   ademas hay que agregar que haga la cuenta total
        codigotransaccion[2],                               #   de lo que debe el cliente
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
    # else:                                             # todo: el objetivo es si no coincide apellido, nombre o cuit
    #     print("No se encontro el valor buscado.")     #       en la realidad se fija si cuit coincide con palabrabuscada
    #                                                           y asi con los otros argumentos. entonces
    #                                                           siempe pasa que encuentra 1 pero falla en los
    #                                                           3 que no coinciden con la busqueda
    # return

# .......................CUENTAS TRANSACCIONES...........................


def precioproducto(codigoproducto):
    if tryproductoexiste(codigoproducto) == False:
        return
    else:
        precio = productList[codigoproducto]["Precio"]
        return precio


def calculartransaccion(codigotransaccion):
    if trytransaccionexiste(codigotransaccion) == False:
        return                                              # fixme: idem consultarcliente
    else:
        totaltransaccion = 0
        cantidaddeitemstransaccion = len(transaccionList[codigotransaccion]["Product List"]) + 1
        for ProductListItem in range(1, cantidaddeitemstransaccion):
            productoN = transaccionList[codigotransaccion]["Product List"][ProductListItem]["Codigo de producto"]
            precioN = precioproducto(productoN)
            cantidadN = transaccionList[codigotransaccion]["Product List"][ProductListItem]["Cantidad"]
            totaltransaccion = totaltransaccion + precioN * cantidadN
    return totaltransaccion


def calculardeudacliente(codigocliente):
    if tryclienteexiste(codigocliente) == False:
        return
    else:
        totaldeudacliente = 0
        cantidaddetransacciones = len(transaccionList) + 1
        for x in range(1, cantidaddetransacciones):
            if transaccionList[x]["Nro de Cliente"] == codigocliente:
                sumardeuda = calculartransaccion(int(x))
                totaldeudacliente = totaldeudacliente + sumardeuda
        print("El cliente debe %s pesos. " % totaldeudacliente)
        return


# -------------------------------FIN FUNCIONES-----------------------------------

# -------------------------------------------------------------------------------
#                                    MAIN
# -------------------------------------------------------------------------------

print("Bienvenido al programa de clientes. \n")
while True:
    ingresousuario = input("--------------------------------------\n"
                           "MENU PRINCIPAL. \n "
                           "\n"
                           "Elija una opcion: \n "
                           "1-Crear cliente \n "
                           "2-Crear producto \n"
                           "3-Crear transaccion \n"
                           "4-Consultar cliente por CODIGO \n"
                           "5-Buscar cliente por nombre/apellido/CUIT \n"
                           "6-Borrar cliente \n"
                           "7-Borrar producto \n"
                           "8-Borrar transaccion \n"
                           "9-Consultar transaccion por CODIGO \n"
                           "10-Imprimir lista de clientes \n"
                           "11-Imprimir lista de transacciones \n"
                           "12-Calcular transaccion \n"
                           "13-Calcular cuanto debe un cliente"
                           "\n"
                           "Para finalizar, presione N\n"
                           "\n"
                           "Opcion a elegir: ")
    if ingresousuario == "1":
        crearcliente()
    if ingresousuario == "2":
        crearproducto()
    if ingresousuario == "3":
        creartransaccion()
    if ingresousuario == "4":
        consultarcliente(int(input("Ingrese el CODIGO del cliente a buscar: ")))
    if ingresousuario == "5":
        buscarcliente(input("Ingrese nombre/apellido/CUIT del cliente a buscar: "))
    if ingresousuario == "6":
        borrarclientes(int(input("Ingrese el CODIGO del cliente a borrar: ")))
    if ingresousuario == "7":
        borrarproducto(int(input("Ingrese el CODIGO del producto a borrar: ")))
    if ingresousuario == "8":
        borrartransaccion(int(input("Ingrese el CODIGO de la transaccion a borrar: ")))
    if ingresousuario == "9":
        consultartransaccion(int(input("Ingrese el CODIGO de la transaccion a buscar: ")))
    if ingresousuario == "10":
        print(clientList)
    if ingresousuario == "11":
        print(transaccionList)
    if ingresousuario == "12":
        calculartransaccion(int(input("Ingrese el CODIGO de la transaccion a calcular: ")))
    if ingresousuario == "13":
        calculardeudacliente(int(input("Ingrese el CODIGO del cliente a calcular su deuda: ")))
    if ingresousuario == "n" or ingresousuario =="N":
        break
