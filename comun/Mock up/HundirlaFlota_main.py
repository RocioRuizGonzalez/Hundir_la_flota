#Importamos las librerias necesarias para ejecutar

import time
import pygame
import numpy as np
import 

#Iniciamos el mixer de pygame y asignamos los sonidos a variables
pygame.mixer.init()
impacto = pygame.mixer.Sound("explosion.wav")
agua = pygame.mixer.Sound("watersplash.wav")
salir = pygame.mixer.Sound("goodbye.wav")

# Variable para el tablero
tablero = [[]]

# Variable  para el tamaño de la tablero
tam = 10

# Variable para el número de barcos a colocar
barcos = 10


# Variable para posiciones de los barcos
posicion = [[]]

# Variable para el alfabeto
alfabeto = {"A" : 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7,
 "I": 8, "J": 9, "a" : 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9} 



tablero_impactos_maquina = creartableros()
tablero_impactos_jugador = creartableros()
tablero_barcos_maquina = iniciar_tablero_con_barcos()
tablero_barcos_jugador = iniciar_tablero_con_barcos()

#Iniciar el juego
bienvenida()
turnojugador()

