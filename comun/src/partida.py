import numpy as np
import tableros as t
import constants as cons

'''
Inicio partida
'''
def coord_maquina():
    coordenadas_maquina = tuple(np.random.randint(10, size=2))
    return coordenadas_maquina

def turnomaquina(tablero_barcos_jugador, tablero_impactos_jugador, coordenadas_maquina): 
    if tablero_barcos_jugador[coordenadas_maquina] == "O":
        tablero_barcos_jugador[coordenadas_maquina] = "X"
        tablero_impactos_jugador[coordenadas_maquina] = "X"
        print("La maquina ha acertado!")
        t.imprimir_tablero(tablero_impactos_jugador)
        coordenadas_maquina = coord_maquina()

    elif tablero_barcos_jugador[coordenadas_maquina] == " ":
        tablero_barcos_jugador[coordenadas_maquina] = "-"
        tablero_impactos_jugador[coordenadas_maquina] = "-"
        print ("La maquina ha dado en agua!")
        t.imprimir_tablero(tablero_impactos_jugador)
        coorden = iniciarjuego()

    elif tablero_barcos_jugador[coordenadas_maquina] == "-":
        tablero_barcos_jugador[coordenadas_maquina] = "-"
        tablero_impactos_jugador[coordenadas_maquina] = "-"
        print ("La maquina ha dado en agua!")
        t.imprimir_tablero(tablero_impactos_jugador)
        coorden = iniciarjuego()  
    else:
        print ("Por favor introduce un numero valido!")

'''
Creación función de juego que interactua con el jugador, especificando que hacer en cada uno de los 3 casos: 
'''

def iniciarjuego():
    coord1 = int(input("Introduce número, por favor: "))
    letra = input("Introduce letra, por favor: ")
    coord2 = cons.alfabeto[letra]
    coorden = tuple([coord1,coord2])
    return coorden
#añadir time


def turnojugador(tablero_barcos_maquina, tablero_impactos_maquina, coorden):
    if tablero_barcos_maquina[coorden] == "O":
        tablero_barcos_maquina[coorden] = "X"
        tablero_impactos_maquina[coorden] = "X"
        print("Has acertado!")
        t.imprimir_tablero(tablero_impactos_maquina)
        coorden = iniciarjuego()

    elif tablero_barcos_maquina[coorden] == " ":
        tablero_barcos_maquina[coorden] = "-"
        tablero_impactos_maquina[coorden] = "-"
        print ("Has dado en agua!")
        t.imprimir_tablero(tablero_impactos_maquina)
        coordenadas_maquina = coord_maquina()

    elif tablero_barcos_maquina[coorden] == "-":
        tablero_barcos_maquina[coorden] = "-"
        tablero_impactos_maquina[coorden] = "-"
        print ("Has vuelto a dar en agua!")
        t.imprimir_tablero(tablero_impactos_maquina) 
        coordenadas_maquina = coord_maquina()  
        
    elif tablero_barcos_maquina[coorden] == "q":
        print ("Has cerrado el juego")        
        
    else:
        print ("Por favor introduce un numero valido!")
        coorden = iniciarjuego()