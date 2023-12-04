#and
print("Sera 'True' solo si los dos valores son verdaderos, de lo contrario sera 'False'")
print("True and True ->", True and True) #True
print("True and False ->", True and False) #False
print("False and True ->", False and True) #False
print("False and False ->", False and False) #False

print(10 > 5 and 5 < 10) #True
print(10 > 5 and 5 > 10) #False

stock = input("Ingrese el numero de stock -> ") #Hay que escribir un valor en "input"
stock = int(stock)                              #Aca transformamos la variable a "int", osea a número 
print(stock >= 100 and stock <= 1000)           #dependiendo de lo que escribimos en "input" va a devolver "True" ó "False"

#or
print("Sera 'True' solo si uno de los valores es verdadero, de lo contrario sera 'False'")
print("True or True ->", True or True) #True
print("True or False ->", True or False) #True
print("False or True ->", False or True) #True
print("False or False ->", False or False) #False

role = input("Digita el rol ->")             #escribir un rol
print(role == "admin" or role == "seller")   #sera verdadero si digitamos "admin" ó "seller" y falso si escribimos lo contrario