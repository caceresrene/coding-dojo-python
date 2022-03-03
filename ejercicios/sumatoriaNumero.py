# Dado un input de numeros devolver la suma de todos ellos
# ex: input -> 1234, output -> 10

entrada = input('Ingrese numero: ')
acum = 0
for letra in entrada:
  acum += int(letra)
print(acum)