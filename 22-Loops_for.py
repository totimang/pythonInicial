for element in range(20):       #el range inicia siempre desde el 0 y termina en el valor 19, porque el 20 es un valor no incluido.
    print(element)

for element in range(1,21):     #indicamos que el range inicie en el 1 y termina en el valor 20, porque el 21 es un valor no incluido.
    print(element)

my_list = [23, 45, 67, 89, 43]
for element_1 in my_list:
    print(element_1)

my_tuple = ("Rodrigo", "Damián", "Gastón")
for element_2 in my_tuple:
    print(element_2)

product = {
    "name": "Camisa",
    "price": 100,
    "stock": 89
}
for key in product:
    print(key,"-->", product[key])  #me devuelve la clave y el valor.

for key, value in product.items():  #me devuelve la clave y el valor, de manera mas sencilla.
    print(key, "-->", value)

people = [
    {
        "name": "Rodrigo",
        "age": 35
    },
    {
        "name": "Damián",
        "age": 34
    },
    {
        "name": "Diego",
        "age": 36
    }
]
for person in people:
    print("name -->", person["name"])