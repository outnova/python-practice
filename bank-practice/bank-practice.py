bobeda_banco = 10000

class cliente:
    def __init__(self, nombre, apellido, n_cuenta, cedula, balance):
        self.nombre = nombre
        self.apellido = apellido
        self.n_cuenta = n_cuenta
        self.cedula = cedula
        self.balance = balance
    def depositar_dinero(self, balance):
        global bobeda_banco
        if(balance > 0):
            self.balance += balance
            bobeda_banco += balance
            print(f"Cliente {self.n_cuenta} deposito {balance}$ en tu cuenta")
        else:
            print("Solo puedes depositar mas de 1$")
    def retirar_dinero(self, balance):
        global bobeda_banco
        if(self.balance >= balance):
            self.balance -= balance
            bobeda_banco -= balance
            print(f"Cliente {self.n_cuenta} retiro {balance}$ de tu cuenta")
        else:
            print("No tienes esta cantidad en tu cuenta")
    def consultar_cuenta(self):
        print(f"Saldo actual: {self.balance}$")

class empleado:
    def __init__(self, nombre, apellido, cedula, cargo):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.cargo = cargo
    def impimir_carnet(self):
        print("Carnet de empleado")
        print(f"Nombre y apellido: {self.nombre} {self.apellido}")
        print(f"Cargo: {self.cargo}")

def consultar_bobeda():
    bobeda = f"Dinero en la bobeda: {bobeda_banco}$"
    print(bobeda)

consultar_bobeda()
Persona1 = cliente("Julio", "Iglesias", 1, 984134, 300)

Persona1.depositar_dinero(500)
Persona1.consultar_cuenta()

consultar_bobeda()

Persona1.retirar_dinero(800)
Persona1.consultar_cuenta()

consultar_bobeda()

Empleado1 = empleado("Carlos", "Lopez", 128989, "Gerente")
Empleado2 = empleado("Maria", "Salas", 891982, "Subgerente")
Empleado3 = empleado("Marcos", "Ruiz", 519898, "Cajero")

Empleado1.impimir_carnet()
Empleado2.impimir_carnet()
Empleado3.impimir_carnet()