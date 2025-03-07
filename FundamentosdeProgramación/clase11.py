a = [1,2,3,4,5]
b = a
print(a)
print(b)
# resultado [1, 2, 3, 4, 5]
#           [1, 2, 3, 4, 5]
del a[0]
# modificamos e eliminamos 
print(id(a))
print(id(b))# agregando id para saber que se devuelve 
# imprimimos ambas listas 
# resultado [2, 3, 4, 5]
c = a[:]
print(id(a))
print(id(b))
print(id(c))
a.append(6)
# se agrega el 6 al final 
print(a)
print(b)
print(c)