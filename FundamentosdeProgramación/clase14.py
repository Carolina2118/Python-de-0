
#################----- diccionario: clave y valor -----###############

numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers)
information = {"nombre":"Carolina",
               #clave    #valor
               "Apellido":"Lobos",
               "Altura":"1.60",
               "Edad":"42"}
print(information)
del information["Edad"] # pido con del eliminar 
print(information)
claves = information.keys()
# es un método que se usa con los diccionarios para obtener
# una vista de todas las claves (keys) dentro de un diccionario.
print(claves)
#print(type (claves))#consultar dato
#cunsultar valore
valor = information.values()# preguntamos los valores
print(valor)
pairs = information.items() #separo valeres y claves por duplas.
print(pairs)

#######################################

contacts = contacts = {"Carla": {"Apellido": "Florida",
               "Altura": 1.60,
               "Edad": 29},
               
                "Diego": {"Apellido": "Antezana",
               "Altura": 1.80,
               "Edad": 32}}

print(contacts)# todo el contacto 
print(contacts["Diego"])# solo datos de lo que se pide ej: diego
print(["Carla"])