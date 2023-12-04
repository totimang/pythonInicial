text = "Ella sabe programar en Python"

'''
print("JavaScript" in text)
print("Python" in text)

if "JS" in text:
    print("Elegiste bien!!!")
else:
    print("También elegiste bien!")
'''

size = len(text)
print(size)


print(text)                         #imprime el texto
print(text.upper())                 #Transforma el texto en letras mayúsculas
print(text.lower())                 #Transforma el texto en letras minúsculas
print(text.count('a'))              #Cuenta cuantas letras 'a' hay en el texto
print(text.swapcase())              #Cambia las mayúsculas por minúsculas y viceversa
print(text.startswith("Ella"))      #Pregunta si la primer palabra del texto es "Ella" en caso de que sea, devuelve "True" sino "False"
print(text.endswith("Rust"))        #Pregunta si la última palabra del texto es "Rust" en caso de que sea, devuelve "True" sino "False"
print(text.replace("Python", "Go")) #Reemplaza la palabra "Python" por la palabra "Go" en el texto

text_2 = "este es un titulo"
print(text_2)                       #Imprime el texto2
print(text_2.capitalize())          #Pone el primer carácter en mayúscula
print(text_2.title())               #Pone el inicio de c/palabra en mayúscula
print(text_2.isdigit())             #Nos dice si el texto es un dígito, devuelve "True" si fuera cierto, sino devuelve "False"
print("398".isdigit())              #hacemos la prueba con números, aunque este en string, para saber si nos toma como un dígito