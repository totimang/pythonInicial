text = "Ella sabe Python"
print(text[0])              #Nos devuelve la letra 'E'.
print(text[1])              #Nos devuelve la letra 'l'.
#print(text[999])            #Nos da error, posición fuera de rango.

size = len(text)            #calcula el tamaño de la variable text.
print("size -> ", size)     #Imprimir el tamaño de la variable text.
print(text[size - 1])       #resta una posición del tamaño total y nos devuelve la letra.

print(text[-1])             #Lo mismo de la linea 6, 7 y 8, pero en una sola linea: resta una posición del tamaño total y nos devuelve la letra.

#slicing
print(text[0:5])            #Nos devuelve el subtexto que hay desde la posición 0 hasta la posición 5.
print(text[10:16])          #Nos devuelve el subtexto que hay desde la posición 10 hasta la posición 16.
print(text[:10])            #Nos devuelve el subtexto que hay desde la posición 0 hasta la posición 10. Al no poner nada de lado izq, se entiende que es 0.
print(text[5:])             #Nos devuelve el subtexto que hay desde la posición 5 hasta el final de la cadena. Al no poner nada de lado der, se entiende que es el final.
print(text[:])              #Nos devuelve el subtexto que hay desde el inicio hasta el final de la cadena. Al no poner nada de lado der/izq, se entiende que es el inicio/final.
print(text[10:16:1])        #nos devuelve el subtexto que desde la posición 10 a la 16. Saltando 1 letra a la vez.
print(text[10:16:2])        #nos devuelve el subtexto que desde la posición 10 a la 16. Saltando 2 letras a la vez.
print(text[::2])            #nos devuelve el subtexto que desde el inicio hasta el final. Saltando 2 letras a la vez