class Usuario:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.balance_cuenta = 0

  def hacer_deposito(self, amount):
    self.balance_cuenta += amount

  def hacer_retiro(self, amount):
    self.balance_cuenta -= amount

  def mostrar_balance_usuario(self):
    print(f'User:{self.name}, Balanace: ${self.balance_cuenta}')
  
  def transfer_dinero(self, other_user, amount):
    self.hacer_retiro(amount)
    other_user.hacer_deposito(amount)

# code
jane = Usuario('Jane', 'jane@doe.com')
jane.hacer_deposito(50)
jane.hacer_deposito(50)
jane.hacer_deposito(50)
jane.hacer_retiro(50)
jane.mostrar_balance_usuario()

john = Usuario('John', 'john@doe.com')
john.hacer_deposito(10)
john.hacer_deposito(200)
john.hacer_retiro(50)
john.hacer_retiro(50)
john.mostrar_balance_usuario()

rene = Usuario('Rene', 'rene@outlook.my')
rene.hacer_deposito(550)
rene.hacer_retiro(50)
rene.hacer_retiro(50)
rene.hacer_retiro(50)
rene.mostrar_balance_usuario()

jane.transfer_dinero(rene, 50)
jane.mostrar_balance_usuario()
rene.mostrar_balance_usuario()