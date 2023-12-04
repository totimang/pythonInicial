print(not True) #devuelve el resultado contrario
print(not False) #devuelve el resultado contrario

print("Al estar usando 'not', sera 'False' solo si los dos valores son verdaderos, de lo contrario sera 'True'")
print("True and True ->", not (True and True)) #False
print("True and False ->", not (True and False)) #True
print("False and True ->", not (False and True)) #True
print("False and False ->", not (False and False)) #True

stock = input("Ingrese el numero de stock -> ") #Hay que escribir un valor en "input"
stock = int(stock)                              #Aca transformamos la variable a "int", osea a número 
print(not (stock >= 100 and stock <= 1000))     #al usar 'not' dependiendo de lo que escribimos en "input" va a devolver "True" ó "False"