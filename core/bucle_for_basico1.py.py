# Basico - numeros enteros del 1 al 150
i = 1
for i in range(151):
  print(i)

# Multiplos de 5 - numeros enteros multiples de 5 entre 5 y 1000
i = 5
while i < 1001:
  if i%5==0:
    print(i)
  i+=1

# Contar, a la manera del dojo - números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo"
i = 1
while i < 101:
  if i%5==0:
    print('Coding')
  if i%10==0:
    print('Coding Dojo')
  else:
    print(i)
  i+=1

# Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
i = 0
acum = 0
while i < 500001:
  if not i%2==0:
    acum += i
  i+=1
print(f'suma total de impares: {acum}')

# Cuenta regresiva de a 4 - imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
i = 2018
while i > 0:
  i -= 4
  (i > 0) and print(i) # si se cumple la asignacion de la izquierda, ejecuta la derecha

# Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas).
print('Contador flexible: (lowNum=2, highNum=9 y mult=3)')
def contadorFlexible(lowNum, highNum, mult):
  i = lowNum
  while i < highNum + 1:
    (i%mult == 0) and print(i)
    i += 1

contadorFlexible(2,9,3)