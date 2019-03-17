class cliente:
    codigo = 0
    apellido = ""
    nombre = ""
    CUIT = ""


class transaccion:
    numero = 0
    fecha = ""
    nombreproducto = ""  # suponiendo que vendes un unico producto con un precio unico
    importe = ""


def crearcliente():
    print("Ahora se creara un nuevo cliente.")

    clientenuevo = cliente
    clientenuevo.codigo = 3   # mostrar el numero de cliente creado
    clientenuevo.apellido = input("Ingrese el apellido del cliente: ")
    clientenuevo.nombre = input("Ingrese el nombre del cliente: ")
    clientenuevo.CUIT = input("Ingrese la CUIT del cliente: ")

    return print("Se creo un nuevo cliente con: n°: %s \n %s, %s. \n CUIT: %s \n"
            % (clientenuevo.codigo,
               clientenuevo.apellido,
               clientenuevo.nombre,
               clientenuevo.CUIT)
                )


def creartransaccion():
    pass


def consultarcliente(consulta):
    return print(
            "El cliente n°: %s \n %s, %s. \n CUIT: %s \n"
            % (consulta.codigo,
               consulta.apellido,
               consulta.nombre,
               consulta.CUIT)
                )


def consultartransaccion(consulta):
    return print(
            "La transaccion n°: %s \n en la fecha: %s.\n Producto: %s. \n Importe total: %s \n"
            % (consulta.numero,
               consulta.fecha,
               consulta.nombreproducto,
               consulta.importe)
                )


# -------------------------
# clientes harcodeados

cliente1 = cliente()
cliente1.codigo = 1
cliente1.apellido = "Arocena"
cliente1.nombre = "Juan Manuel"
cliente1.CUIT = "30-25125842-2"

cliente2 = cliente()
cliente2.codigo = 2
cliente2.apellido = "Villar"
cliente2.nombre = "Sandra"
cliente2.CUIT = "23-251152842-2"


# -------------------------
# transacciones harcodeadas

transaccion1 = transaccion
transaccion1.codigo = 1
transaccion1.fecha = "22 de marzo del 2015"
transaccion1.nombreproducto = "remera estampada"
transaccion1.importe = 4500.00

transaccion2 = transaccion
transaccion2.codigo = 2
transaccion2.fecha = "17 de abril del 2016"
transaccion2.nombreproducto = "taza ploteada"
transaccion2.importe = 1500.00

# -------------------------

consultarcliente(cliente2)
consultartransaccion(transaccion1)

crearcliente()



# -------------------------
'''
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 
'''
