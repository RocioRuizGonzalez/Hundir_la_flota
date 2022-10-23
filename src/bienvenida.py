import time
import pygame
pygame.mixer.init()

'''
Función de bienvenida al juego, que presenta a los jugadores 
'''
def bienvenida():
    salir = pygame.mixer.Sound("../media/goodbye.wav")
    print("Bienvenido al juego de Hundir la flota")
    nombre_jugador = input("Introduce tu nombre por favor: ")
    print(f"Hola {nombre_jugador}, tu oponente es Popeye")
    time.sleep(2)
    print("Empieza la partida ¡Que gane el mejor!")
    salir.play()