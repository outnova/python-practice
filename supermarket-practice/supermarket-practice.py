porcentaje_iva = 0.16
class empleado:
    def __init__(self, nombre, apellido, cedula, cargo, turno):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.cargo = cargo
        self.turno = turno
    def imprimir_carnet(self):
        print("Carnet de empleado")
        print(f"{self.nombre} {self.apellido}")
        print(f"C.I. {self.cedula}")
        print(f"Cargo: {self.cargo}")
class producto:
    def __init__(self, serial, nombre, precio, descripcion):
        self.serial = serial
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
    def imprimir_producto(self): #imprimir info del producto
        print(f"Serial: {self.serial}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")

class cliente:
    lista_productos = []
    def __init__(self, id, nombre, apellido, cedula, direccion):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.direccion = direccion
    def imprimir_cliente(self): #imprime los datos del cliente
        print("Datos del cliente:")
        print(f"ID: {self.id}")
        print(f"Nombre y apellido: {self.nombre} {self.apellido}")
        print(f"Cedula: {self.cedula}")
        print(f"Direccion: {self.direccion}")
    def comprar_producto(self, serial, cantidad):
        for prod in self.lista_productos:  # Accedemos a lista_productos como un atributo de clase
            if prod.serial == serial:
                iva = 0.16
                precio_total = prod.precio * cantidad
                factura = f"Cliente {self.id} Ha comprado {cantidad} unidades de {prod.nombre}"
                print(factura)
                iva = precio_total * porcentaje_iva
                precio_totalito = precio_total + iva
                print(f"Monto pagado: {precio_total}$")
                print(f"IVA ({porcentaje_iva * 100}%): {iva}$")
                print(f"Total a pagar: {precio_totalito}$")
                break
        else:
            print("No se encontró un producto con el serial especificado") 
        
Empleado1 = empleado("Daniel", "Garcia", 1925189, "Cajero", "Tarde")
Empleado2 = empleado("Maria", "Mercedes", 2591991, "Cajera", "Tarde")

Franela = producto(1, "Franela manga corta", 10, "Franelita")

cliente.lista_productos = [Franela]

Cliente1 = cliente(1, "Francisco", "Lopez", 1894589, "Avenida 82 con calle 3")
Cliente2 = cliente(2, "Enrique", "Suarez", 1234989, "Calle 9 con calle 4 transversal 2")

Cliente1.comprar_producto(1, 2)