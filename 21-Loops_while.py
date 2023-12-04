'''
while True:
    print("se ejecuto") #se va a ejecutar un bucle infinito. con Ctrl+C detenemos el bucle en consola.
'''

counter = 0         #que la variable empiece en 0.
while counter < 10: #definimos la condición.
    counter += 1    #le decimos que sume 1.
    print(counter)  #va a imprimir desde el 0 y le va a sumar 1 hasta que llegue al 10, luego termina el bucle.

counter_2 = 0
while counter_2 < 20:
    counter_2 += 1
    if counter_2 == 14:
        break       #una forma forzada de cortar ese flujo.
    print(counter_2)

counter_3 = 0
while counter_3 < 20:
    counter_3 += 1
    if counter_3 < 16:
        continue    #tenemos la impresión del 16 al 20
    print(counter_3)