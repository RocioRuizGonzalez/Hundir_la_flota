import time
import pygame
pygame.mixer.init()
salir = pygame.mixer.Sound("goodbye.wav")

'''
Función de bienvenida al juego, que presenta a los jugadores 
'''

def bienvenida():
    salir = pygame.mixer.Sound("goodbye.wav")
    print("Bienvenido al juego de Hundir la flota")
    nombre_jugador = input("Introduce tu nombre por favor: ")
    print(f"Hola {nombre_jugador}, tu oponente es Popeye")
    time.sleep(2)
    print("Empieza la partida ¡Que gane el mejor!")