laberinto = [
[' ', 'X', 'X', 'X', 'X'],
[' ', 'X', ' ', ' ', ' '], 
[' ', 'X', ' ', 'X', ' '], 
[' ', ' ', ' ', 'X', ' '], 
['X', 'X', 'X', 'X', 'S']
]

def laberinto(dimension, muro):
    laberinto=[]
    for i in range(dimension):
        fila=[]
        for j in range(dimension):
            if (i, j) in muro:
                fila.append("x")
            else:
                fila.append(" ")
        laberinto.append(fila)
    return(laberinto)


muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))