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


class Usuario:
    def __init__(self, name, email, tasaDeInteres):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria(tasaDeInteres)

    def hacer_deposito(self, amount):
      self.cuenta.deposito(amount)
      return self

    def hacer_retiro(self, amount):
        self.cuenta.deposito(amount)
        return self

    def mostrar_balance_usuario(self):
        print(f'User: {self.name}, Balance: {self.cuenta.balance}')
        return self

    def transfer_dinero(self, other_user, amount):
        self.hacer_retiro(amount)
        other_user.deposito(amount)
        return self


john = Usuario('John Doe', 'john@doe.xyz', 0.01)

johnOtherBank = CuentaBancaria(0.33)

john.hacer_deposito(50)
john.mostrar_balance_usuario()