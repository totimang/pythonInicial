matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[0])    #nos indique que elemento hay de la posición 0 y nos devuelve una la lista.
print(matriz[0][1]) #nos indique que elemento hay de la posición 0 y coordenada 1, nos devuelve un número. Fila 0, columna 1

for row in matriz:
    print(row)
    for column in row:
        print(column)