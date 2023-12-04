#CRUD Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])

numbers[-1] = 10 #cambia el ultimo valor de la lista, por el nuevo valor asignado.
print(numbers)

numbers.append(700) #agrega un elemento nuevo al final de la lista.
print(numbers)

numbers.insert(0, "hola") #estoy dando 2 valores, el 1ero es la posición de mi lista y el 2do lo que quiero agregar. Y luego lo agrega en mi lista al imprimirlo.
print(numbers)

numbers.insert(3, "change") #coloca el valor en la posición 3, pero corre los valores hacia la izquierda, no los borra
print(numbers)

task = ["todo 1", "todo 2", "todo 3"]
new_list = numbers + task #puedo fusionar las listas.
print(new_list)

index = new_list.index("todo 2")
new_list[index] = "todo changed"
print(new_list)

new_list.remove("todo 1") #elimina el elemento que nosotros queremos.
print(new_list)

new_list.pop() #elimina el ultimo elemento de la lista.
print(new_list)

new_list.pop(0) #al darle el parámetro de la posición eliminamos el elemento especifico.
print(new_list)

new_list.reverse() #me devuelve la lista al revés.
print(new_list)

numbers_a = [1, 4, 6, 3]
numbers_a.sort() #me ordena los números de menor a mayor.
print(numbers_a)

strings = ["re", "ab", "ed"]
strings.sort() #me ordena las silabas desde la 'a' a la 'z'
print(strings)

new_list.sort()
#print(new_list) #saldrá ERROR, porque tiene tipos de datos mezclados números/letras