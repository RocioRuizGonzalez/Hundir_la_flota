


import time
import pygame
import numpy as np

#Iniciamos el mixer de pygame y asignamos los sonidos a variables
pygame.mixer.init()
impacto = pygame.mixer.Sound("explosion.wav")
agua = pygame.mixer.Sound("watersplash.wav")
salir = pygame.mixer.Sound("goodbye.wav")


import creartableros()
import iniciar_tablero_con_barcos()
import imprimir_tablero()
import turnojugador()

tablero_impactos_maquina = creartableros()
imprimir_tablero(tablero_impactos_maquina)
tablero_impactos_jugador = creartableros()
imprimir_tablero(tablero_impactos_maquina)

tablero_barcos_maquina = iniciar_tablero_con_barcos()
tablero_barcos_jugador = iniciar_tablero_con_barcos()
imprimir_tablero(tablero_barcos_maquina) 
imprimir_tablero(tablero_barcos_jugador)
'''
Definicion de funcion del juego que interactúa con el jugador
'''
def juegomaquina(): 
    while "O" in tablero_barcos_maquina and "O" in tablero_barcos_jugador: 
        #Genera coordenadas aleatorias para los disparos de la maquina
        coordenadas_maquina = tuple(np.random.randint(10, size=2))

        #Establece la condición de seguir ejecutando el bucle mientras hayan barcos en el tablero de ambos jugadores
        if tablero_barcos_jugador[coordenadas_maquina] == "O":
            tablero_barcos_jugador[coordenadas_maquina] = "X"
            tablero_impactos_jugador[coordenadas_maquina] = "X"
            time.sleep(1)
            print("La maquina ha acertado!")
            impacto.play()
            time.sleep(2)
            imprimir_tablero(tablero_impactos_jugador)
            continue

        elif tablero_barcos_jugador[coordenadas_maquina] == " ":
            tablero_barcos_jugador[coordenadas_maquina] = "-"
            tablero_impactos_jugador[coordenadas_maquina] = "-"
            time.sleep(1)
            print ("La maquina ha dado en agua!")
            agua.play()
            time.sleep(2)
            imprimir_tablero(tablero_impactos_jugador)
            turnojugador()
            

        elif tablero_barcos_jugador[coordenadas_maquina] == "-":
            tablero_barcos_jugador[coordenadas_maquina] = "-"
            tablero_impactos_jugador[coordenadas_maquina] = "-"
            time.sleep(1)
            print ("La maquina ha dado en agua!")
            agua.play()
            time.sleep(2)
            imprimir_tablero(tablero_impactos_jugador)
            turnojugador()
        else:
            break
    #Bucle que define el comportamiento de no haber barcos en algunos de los dos tableros:     
    if "O" not in tablero_barcos_jugador:
        print("Lo siento! Has perdido la partida")

    elif "O" not in tablero_barcos_maquina:
        print("Enhorabuena! Has ganado la partida")
