if True:
    print("Debería ejecutarse")

if False:
    print("Nunca se ejecuta")

pet = input("¿Cuál es tu mascota favorita?")
if pet == "perro":
    print("Genial tenes un buen gusto")
elif pet == "gato":
    print("Espero tengas suerte")
elif pet == pez:
    print("Eres lo máximo")
else:
    print("No tienes ninguna mascota interesante")

stock = input("Digita el stock -> ")
stock = int(stock)
if stock >= 100 and stock <= 1000:
    print("El stock es correcto")
else:
    print("El stock es incorrecto")