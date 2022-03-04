
# ! cuantas veces se repite una letra
def cuantasLetras(string):
  diccionario = {}
  for letra in string:
    # si hay un espacio vacio, saltalo
    if letra == ' ':
      continue

    # si existe la entrada letra en el diccionario, suma
    if letra in diccionario:
      diccionario[letra] +=1
    else: # si no existe, iniciala en 1
      diccionario[letra] = 1
  return diccionario

print(cuantasLetras('buenos dias'))

# ! Cuantas veces se repite una palabra
def encuentraPalabra(arr, palabra):
  contador = 0
  for index in arr:
    if index == palabra:
      contador += 1
  return contador

print(encuentraPalabra(['me', 'me', 'meow'], 'me'))
