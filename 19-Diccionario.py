my_dict = {}
print(type(my_dict))

my_dict = {
    "avion": "bla bla bla",
    "name": "Rodrigo",
    "last_name": "Martinez",
    "age": 35,
}

print(my_dict)
print(len(my_dict))         #Me dice cuántos elementos hay en este diccionario.

print(my_dict["age"])       #me dice que valor esta en "age".
print(my_dict["last_name"]) #me dice que valor esta en "last_name".
#print(my_dict["casa"])     #al escribir otro valor, me devuelve un ERROR. Por eso es mejor escribir con el .get
print(my_dict.get("age"))   #me dice que valor esta en "age".
print(my_dict.get("casa"))  #al escribir otro valor, me devuelve "none".

print("avion" in my_dict)   #al escribir un elemento y si se encuentra en mi diccionario, me devuelve "True".
print("casa" in my_dict)    #al escribir un elemento y si no se encuentra en mi diccionario, me devuelve "False".