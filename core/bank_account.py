class CuentaBancaria:
    cuentas = 0

    def __init__(self, tasa_interes, balance=0):
        self.balance = balance
        self.tasa_interes = tasa_interes
        CuentaBancaria.cuentas += 1

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if (self.balance > amount):
            self.balance -= amount
        else:
            print(
                f'Fondos insuficientes: cobrando una tarifa de ${self.balance} y resta ${amount}')
        return self

    def mostrar_info_cuenta(self):
        print(f'Balance: ${self.balance}')
        return self

    def generar_interes(self):
        if (self.balance > 0):
            self.balance = self.balance + self.balance * self.tasa_interes
        return self

    @classmethod
    def getCuentas(cls):
        print(cls.cuentas)


john = CuentaBancaria(0.01)
john.deposito(50).deposito(50).deposito(50).retiro(20).mostrar_info_cuenta()

jane = CuentaBancaria(0.02)
jane.deposito(50).deposito(50).retiro(10).retiro(10).retiro(
    10).retiro(10).generar_interes().mostrar_info_cuenta()

CuentaBancaria.getCuentas()