x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# 1.Actualizar valores en diccionarios y listas
def actualizarValores():
  x[1][0] = 15
  estudiantes[0]['last_name'] = 'Bryant'
  directorio_deportes['fútbol'][0] = 'Andrés'
  z[0]['y'] = 30
actualizarValores()


estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# 2.Iterar a través de una lista de diccionarios
def iterateDictionary(some_list):
  for dictionary in some_list:
    for key in dictionary:
      print(f'{key} - {dictionary[key]}')
iterateDictionary(estudiantes)

# 3.Obtener valores de una lista de diccionarios
def iterateDictionary2(key_name, some_list):
  for dictionary in some_list:
    print(dictionary[key_name])
iterateDictionary2('first_name', estudiantes)

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# 4.Iterar a través de un diccionarios con valores de lista
def printInfo(some_dict):
  for key in some_dict:
    print(len(some_dict[key]) ,key.upper())
    for index in some_dict[key]:
      print(index)
printInfo(dojo)