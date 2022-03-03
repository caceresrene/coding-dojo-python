class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        return self

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
        return self

    def mostrar_balance_usuario(self):
        print(f'User:{self.name}, Balanace: ${self.balance_cuenta}')
        return self

    def transfer_dinero(self, other_user, amount):
        self.hacer_retiro(amount)
        other_user.hacer_deposito(amount)
        return self


# code
jane = Usuario('Jane', 'jane@doe.com').hacer_deposito(50).hacer_deposito(50).hacer_deposito(50).hacer_retiro(50).mostrar_balance_usuario()

john = Usuario('John', 'john@doe.com').hacer_deposito(10).hacer_deposito(200).hacer_retiro(50).hacer_retiro(50).mostrar_balance_usuario()

rene = Usuario('Rene', 'rene@outlook.my')
rene.hacer_deposito(550).hacer_retiro(50).hacer_retiro(50).hacer_retiro(50).mostrar_balance_usuario()

jane.transfer_dinero(rene, 50).mostrar_balance_usuario()
rene.mostrar_balance_usuario()
