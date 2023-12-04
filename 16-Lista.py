numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ["make a dishes", "play videogames"]
print(tasks)

type= [1, True, "hola"]
print(type)

print(numbers[0])
print(tasks[0])

text = "hola"
#text[0] = 'w' #los strings no son mutables

tasks[0] = "watch platzi courses"
print(tasks) #las listas son mutables

tasks[0] = "do the dishes"
print(tasks)

print(numbers[:3])
print(True in type) #busca si esta la palabra "True" dentro de la lista "type" y si esta, devuelve --> True
print("hola" in type) #busca si esta la palabra "hola" dentro de la lista "type" y si esta, devuelve --> True