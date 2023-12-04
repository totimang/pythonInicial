person = {
    "name": "Rodrigo",
    "last_name": "Martinez",
    "langs": ["Python", "JavaScript"],
    "age": 35,
}

print(person)

person["name"] = "Damián"       #me cambia el nombre.
person["twitter"] = "@totimang" #me agrega un nuevo elemento al diccionario.
person["age"] -= 10             #resta 10 años a mi edad actual.
person["langs"].append("Java")  #agrega un lenguaje en la ultima posición.
print(person)

del person["last_name"]         #elimina el atributo mencionado "last_name".
person.pop("age")               #elimina el atributo mencionado "age", si o si hay que escribirlo dentro del paréntesis o devuelve ERROR.
print(person)

print("items")
print(person.items())           #me genera una tupla.

print("keys")
print(person.keys())            #me devuelve una lista con las/os llaves/atributos.

print("values")                 #me devuelve una lista con los valores.
print(person.values())