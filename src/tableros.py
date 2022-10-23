import numpy as np


'''
Definir la función para la generación de tablero en el juego
'''

def creartableros():
    tablero = np.full((10, 10), ' ')
    return tablero

'''
Generación de tableros con barcos aleatorios
'''
def iniciar_tablero_con_barcos():
    tablero=np.full((10,10), " ")
    barcos=[1,1,1,1,2,2,2,3,3,4]
    i=0
    while i<len(barcos):
        exito = False
        while not exito:
            exito = colocar_barco_aleatoriamente(tablero,barcos[i])
        i=i+1
    return tablero

'''
Colocar barcos aleatoriamente
'''
def colocar_barco_aleatoriamente(tablero, tam):
    posicion = nueva_posicion_barco()
    cabe = comprobar_barco_cabe_en_tablero(tablero, posicion[0], posicion[1], posicion[2], tam)
    if not cabe:
        return False
    else:
        existe = comprobar_existe_barco(tablero, posicion[0], posicion[1], posicion[2], tam)
        if existe:
            return False
        else:
            colocar_barco(tablero, posicion[0], posicion[1], posicion[2], tam)
    return True

'''
Posición aleatoria
'''
def nueva_posicion_barco():
    fila = np.random.randint(0, 10)
    columna = np.random.randint(0, 10)
    orientacion = np.random.randint(0, 4)
    coordenadas = {0:"N", 1:"S", 2: "E", 3:"O"}
    return (fila, columna, coordenadas[orientacion])

'''
Comprobar barco aleatorio cabe en tablero
'''
def comprobar_barco_cabe_en_tablero(tablero, fila, columna, orientacion, tam):
    if orientacion == "E":
        return (columna + (tam-1)) <= (tablero.shape[1] - 1)
    elif orientacion == "O":
        return (columna - (tam-1)) >= 0
    elif orientacion == "N":
        return (fila - (tam-1)) >= 0
    elif orientacion == "S":
        return (fila + (tam-1)) <= (tablero.shape[0] - 1)

'''
Comprobar si existe barco
'''
def comprobar_existe_barco(tablero, fila, columna, orientacion, tam):
    for i in range(tam):
        if orientacion == "E":
            if (tablero[fila, columna+i] == "O") | (tablero[fila, columna+i] == "X"):
                return True
        elif orientacion == "O":
            if (tablero[fila, columna-i] == "O") | (tablero[fila, columna-i] == "X"):
                return True
        elif orientacion == "N":
            if (tablero[fila-i, columna] == "O") | (tablero[fila-i, columna] == "X"):
                return True
        elif orientacion == "S":
            if (tablero[fila+i, columna] == "O") | (tablero[fila+i, columna] == "X"):
                return True
    return False

'''
Colocar barcos aleatoriamente
'''
def colocar_barco(tablero, fila, columna, orientacion, tam):
    for i in range(tam):
        if orientacion == "E":
            tablero[fila, columna+i] = "O"
        elif orientacion == "O":
            tablero[fila, columna-i] = "O"
        elif orientacion == "N":
            tablero[fila-i, columna] = "O"
        elif orientacion == "S":
            tablero[fila+i, columna] = "O"

'''
Generación de tableros
'''
def imprimir_tablero(tablero):
        print("  A B C D E F G H I J")
        i = 0
        for fila in tablero:
               linea_imprimir = str(i) + " " 
               for elemento in fila:
                       linea_imprimir = linea_imprimir + elemento + " "
               print(linea_imprimir)
               i = i + 1