# numeros cuadrados 
# palabra clave in se usa para verificar si un elemento está dentro de algo
# (como una lista, un diccionario, una cadena, etc.) o para recorrer elementos en un bucle.

squares = [x**2 for x in range(1,11)]
print("Cuadrados:", squares)

# se sacara valor de fahrenheit

celsius = [0, 10, 20, 30, 40, 50]
fahrenheit = [(temperatura * 9/5) +32 for temperatura in celsius]

print("RESULTADO TEMPERATURA EN F:",fahrenheit)