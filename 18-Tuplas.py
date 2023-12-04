numbers = (1, 2, 3, 5)
strings = ("nico", "zule", "santi", "nico")
print(numbers)
print("0 ->", numbers[0])
print("-1 ->", numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

#CRUD
#numbers.append(10) #no tiene este método, no se puede modificar, es solo lectura la tupla.
print(numbers)
#numbers[1] = "change" #no tiene este método, no se puede modificar, es solo lectura la tupla.

print(strings)
print(strings.index("zule")) #nos muestra la posición.
print(strings.count("nico")) #nos dice cuántas veces esta esa palabra.

my_list = list(strings)     #transformamos la tupla en una lista."[]"
print(my_list)              #imprimo la lista.
print(type(my_list))        #no imprime el tipo de archivo, en este caso es una lista.

my_list[1] = "juli"         #al ser una lista, podemos agregar un nuevo texto en esa posición '-1'.
print(my_list)

my_tuple = tuple(my_list)   #transformamos la lista en una tupla. "()"
print(my_tuple)