#1. crear una clase Tienda que tenga los siguientes atributos:
    #nombre
    #direccion
    #telefono
    #lista de productos
    #lista de clientes
    #histórico de ventas
class Tienda:
    def __init__(self, nombre,direccion,telefono):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.productos=[]
        self.clientes=[]
        self.ventas=[]
    #definir un método para agregar un nuevo producto
    def agregarProducto(self,producto):
        self.productos.append(producto)
    
    def imprimirProductos(self):
        for producto in self.productos:
            print(producto)

    #definir un método para agregar un nuevo cliente
    def agregarCliente(self,cliente):
        self.clientes.append(cliente)
    
    def imprimirClientes(self):
        for cliente in self.clientes:
            print(cliente)

#2. crear una clase Producto que tenga los siguientes atributos:
    #nombre
    #precio
class Producto:
    def __init__(self,nombre, precio):
        self.nombre=nombre
        self.precio=precio
    
    def __str__(self):
        return self.nombre + " - " + str(self.precio)

#3. crear una clase Cliente que tenga los siguientes atributos:
    #nombre
    #documento
    #lista de compras
class Cliente:
    def __init__(self,nombre,documento):
        self.nombre=nombre
        self.documento=documento
        self.compras=[]

    def __str__(self):
        return self.nombre + " - " + self.documento
    

#4. crear una clase Venta que tenga los siguientes atributos:
    #fecha
    #lista de productos y cantidades
    #cliente
class Venta:
    def __init__(self,cliente,fecha):
        self.cliente=cliente
        self.fecha=fecha
        self.productos=[]


#crear la lógica de la aplicación
tienda = Tienda("Tienda MisionTIC","calle 123","321")

while True:
    instrucciones="""
        ingrese P para agregar un nuevo producto a la tienda
        ingrese IP para imprimir los productos de la tienda
        ingrese C para agregar un nuevo cliente a la tienda
        ingrese IC para imprimir los clientes de la tienda
    """
    operacion = input(instrucciones)
    if operacion == "P":
        nombreProducto=input("ingrese el nombre del producto: ")
        precioProducto=float(input("Ingrese el precio del producto: "))
        nuevoProducto = Producto(nombreProducto,precioProducto)
        tienda.agregarProducto(nuevoProducto)
    elif operacion == "IP":
        tienda.imprimirProductos()
    elif operacion == "C":
        nombreCliente = input("ingrese el nombre del cliente: ")
        documentoCliente = input("ingrese el documento del cliente: ")
        nuevoCliente = Cliente(nombreCliente,documentoCliente)
        tienda.agregarCliente(nuevoCliente)
    elif operacion == "IC":
        tienda.imprimirClientes()