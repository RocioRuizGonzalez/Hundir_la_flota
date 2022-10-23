import time
import pygame
pygame.mixer.init()

'''
Función de bienvenida al juego, que presenta a los jugadores 
'''
def bienvenida():
    salir = pygame.mixer.Sound("../media/goodbye.wav")
    salir.play()
    print (r"""
    
    
    
    
dP     dP                          dP oo             dP              88888888b dP            dP
88     88                          88                88              88        88            88
88aaaaa88a dP    dP 88d888b. .d888b88 dP 88d888b.    88 .d8888b.    a88aaaa    88 .d8888b. d8888P .d8888b.
88     88  88    88 88'  `88 88'  `88 88 88'  `88    88 88'  `88     88        88 88'  `88   88   88'  `88
88     88  88.  .88 88    88 88.  .88 88 88          88 88.  .88     88        88 88.  .88   88   88.  .88
dP     dP  `88888P' dP    dP `88888P8 dP dP          dP `88888P8     dP        dP `88888P'   dP   `88888P8
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                               
                                                                                                                         """)
    print("Bienvenido al juego de Hundir la flota")
    nombre_jugador = input("Introduce tu nombre por favor: ")
    print(f"Hola {nombre_jugador}, tu oponente es Popeye")
    time.sleep(2)
    print("Empieza la partida ¡Que gane el mejor!")
    
