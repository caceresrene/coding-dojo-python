
def esPrimo(num):
  # por cada numero, recorre y chequea que no sea divisible por otro numero
  for n in range(2,num):
    if num % n == 0:
      return False
  return True