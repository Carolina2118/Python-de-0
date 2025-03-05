#lista cosas
to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)
#lista numero// imprime numero como letras en tipo list (palabra clave)
numbers = [1,2,3,4, "cinco"]
print(type(numbers))
# lista dentro de lista 
mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)
# longitud o elementos tiene.
print(len(mix))
# elegir o identificar el primer elemento o posición
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print("Ultimo elemento:", mix[-1])
# elementos de la cadena 
string = "Hola mundo"
print("Primer elemento", string[0])
print("Segundo elemento", string[1])
print("Ultimo elemento:", string[-1])
# puede indicar la Posición de 0 a X que es la final
print(mix[2:-2])
print(mix)
# para añadir o agregar al final de la lista append elemento independiente
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)
# insertar un dato en posición especifico((1= posición ["a","b"]= informacion ))
mix.insert(1,["a","b"])
print(mix)
# indica en que posicion esta la informacion en una lista
print(mix.index(["a","b"]))
numbers = [1,2,100.01,90.45,3,4, 5]
print(numbers)
print("Mayor:",max(numbers))# numero mayor
print("Menor:",min(numbers))# numero menor 
# palabra reservada del y eliminar lista o elemento especifico
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
# elimino lista completa
del numbers
#print(numbers