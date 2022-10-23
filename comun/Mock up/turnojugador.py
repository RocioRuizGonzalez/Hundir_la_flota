

import time
import pygame
import numpy as np
import sys

#Iniciamos el mixer de pygame y asignamos los sonidos a variables
pygame.mixer.init()
impacto = pygame.mixer.Sound("explosion.wav")
agua = pygame.mixer.Sound("watersplash.wav")
salir = pygame.mixer.Sound("goodbye.wav")


from 
import iniciar_tablero_con_barcos()
import imprimir_tablero()
import juegomaquina()

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
def turnojugador():
    #Establece la condición de seguir ejecutando el bucle mientras hayan barcos en el tablero de ambos jugadores
    while "O" in tablero_barcos_maquina and "O" in tablero_barcos_jugador: 

        coord1 =(input("Introduce 1 coordenada del 1 al 10 por favor: "))
        # Try and except que introduce la posibilidad de salir del juego con cualquier otra tecla que no sea int
        try:
            coord1 = int(coord1)
              
        except Exception:
            print("Cerrando juego...")
            time.sleep(2)
            salir.play()
            print("Goodbye")

        if coord1 < 0 or coord1 > 9:
            print("Introduce un número valido por favor")  
            continue  
            
        letra = input("Introduce letra, por favor: ")
        coord2 = alfabeto[letra]
        try:
            coord2 = int(coord2)
            
        except Exception:
            print("Cerrando juego...")
            time.sleep(2)
            salir.play()
            print("Goodbye")
            
        #Se asegura de que el número introducido esté en el rango 
        if coord2 < 0 or coord2 > 9:
            print("Introduce un número valido por favor")
            continue
    

        coorden =tuple([(coord1),(coord2)])

        #Bucle que comprueba la posición de la coordenada introducida
        if tablero_barcos_maquina[coorden] == "O":
            tablero_barcos_maquina[coorden] = "X"
            tablero_impactos_maquina[coorden] = "X"
            print("Has acertado!")
            impacto.play()
            time.sleep(2)
            imprimir_tablero(tablero_impactos_maquina)
            continue

        elif tablero_barcos_maquina[coorden] == "-":
            tablero_barcos_maquina[coorden] = "-"
            tablero_impactos_maquina[coorden] = "-"
            print ("Has vuelto a dar en agua!")
            agua.play()
            time.sleep(2)
            imprimir_tablero(tablero_impactos_maquina)
            juegomaquina()
        
        elif tablero_barcos_maquina[coorden] == " ":
            tablero_barcos_maquina[coorden] = "-"
            tablero_impactos_maquina[coorden] = "-"
            print ("Has dado en agua!")
            agua.play()
            time.sleep(2)
            imprimir_tablero(tablero_impactos_maquina)
            juegomaquina()

       
    #Bucle que define el comportamiento de no haber barcos en algunos de los dos tableros: 
    if "O" not in tablero_barcos_jugador:
        print("Lo siento! Has perdido la partida")

    elif "O" not in tablero_barcos_maquina:
        print("Enhorabuena! Has ganado la partida")

