def laberinto(dimension, muro):
    laberinto=[]
    for i in range(dimension):
        fila=[]
        for j in range(dimension):
            if tuple([i, j]) in muro:
                fila.append("x")
            else:
                fila.append(" ")
                
        laberinto.append(fila)
    return(laberinto)


muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
laberinto1=laberinto(5, muro)

for i in laberinto1:
    print(i)

def recorrerlaberinto(laberinto):
    fila=columna=0
    movimiento= ["abajo"]
    n=5
    while (fila< n-1 and columna<n):

        if movimiento[-1] != "arriba" and fila+1 < n and laberinto[fila +1][columna] != "x":
            fila +=1
            movimiento.append("abajo")
        elif movimiento[-1] != "abajo" and fila-1 < n and laberinto[fila-1][columna] != "x":
            fila -= 1
            movimiento.append("arriba")
        elif movimiento[-1] != "izquierda" and columna +1 < n and laberinto[fila][columna+1] != "x":
            columna += 1
            movimiento.append("derecha")
        elif movimiento[-1] != "derecha" and columna-1 > 0 and laberinto[fila][columna-1] != "x":
            columna -= 1
            movimiento.append("izquierda")
    return(movimiento)


print(recorrerlaberinto(laberinto1))