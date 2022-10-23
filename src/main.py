import numpy as np
import partida as p
import tableros as t
import bienvenida as b
import pygame

pygame.mixer.init()
impacto = pygame.mixer.Sound("explosion.wav")
agua = pygame.mixer.Sound("watersplash.wav")
salir = pygame.mixer.Sound("goodbye.wav")

'''
Iniciación del juego
'''
tablero_impactos_maquina = np.full((10,10), " ")
t.imprimir_tablero(tablero_impactos_maquina)

tablero_impactos_jugador = np.full((10,10), " ")
t.imprimir_tablero(tablero_impactos_jugador)

tablero_barcos_maquina = t.iniciar_tablero_con_barcos()
tablero_barcos_jugador = t.iniciar_tablero_con_barcos()
t.imprimir_tablero(tablero_barcos_maquina)
t.imprimir_tablero(tablero_barcos_jugador)

b.bienvenida()
p.turnojugador(tablero_barcos_maquina, tablero_barcos_jugador, tablero_impactos_maquina, tablero_impactos_jugador)

#coorden = iniciarjuego()
#print(coorden)

#jugador1 = turnojugador(tablero_barcos_maquina, tablero_impactos_maquina, coorden)

#coordenadas_maquina = p.coord_maquina()
#print(coordenadas_maquina)
#turnomaquina = p.turnomaquina(tablero_barcos_jugador, tablero_impactos_jugador, coordenadas_maquina)