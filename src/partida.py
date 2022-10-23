import numpy as np
import tableros as t
import constants as cons
import time
import pygame

pygame.mixer.init()
impacto = pygame.mixer.Sound("../media/explosion.wav")
agua = pygame.mixer.Sound("../media/watersplash.wav")
salir = pygame.mixer.Sound("../media/goodbye.wav")

'''
Definicion de funcion del juego que interactúa con el jugador
'''
def juegomaquina(tablero_barcos_jugador, tablero_barcos_maquina, tablero_impactos_jugador, tablero_impactos_maquina): 
    while "O" in tablero_barcos_maquina and "O" in tablero_barcos_jugador: 
        #Genera coordenadas aleatorias para los disparos de la maquina
        coordenadas_maquina = tuple(np.random.randint(10, size=2))

        #Establece la condición de seguir ejecutando el bucle mientras hayan barcos en el tablero de ambos jugadores
        if tablero_barcos_jugador[coordenadas_maquina] == "O":
            tablero_barcos_jugador[coordenadas_maquina] = "X"
            tablero_impactos_jugador[coordenadas_maquina] = "X"
            time.sleep(1)
            print("¡La maquina ha acertado!")
            impacto.play()
            time.sleep(2)
            t.imprimir_tablero(tablero_impactos_jugador)
            continue

        elif tablero_barcos_jugador[coordenadas_maquina] == " ":
            tablero_barcos_jugador[coordenadas_maquina] = "-"
            tablero_impactos_jugador[coordenadas_maquina] = "-"
            time.sleep(1)
            print ("¡La maquina ha dado en agua!")
            agua.play()
            time.sleep(2)
            t.imprimir_tablero(tablero_impactos_jugador)
            turnojugador(tablero_barcos_maquina, tablero_barcos_jugador, tablero_impactos_maquina, tablero_impactos_jugador)
            

        elif tablero_barcos_jugador[coordenadas_maquina] == "-":
            tablero_barcos_jugador[coordenadas_maquina] = "-"
            tablero_impactos_jugador[coordenadas_maquina] = "-"
            time.sleep(1)
            print ("¡La maquina ha dado en agua!")
            agua.play()
            time.sleep(2)
            t.imprimir_tablero(tablero_impactos_jugador)
            turnojugador(tablero_barcos_maquina, tablero_barcos_jugador, tablero_impactos_maquina, tablero_impactos_jugador)
        else:
            break
    #Bucle que define el comportamiento de no haber barcos en algunos de los dos tableros:     
    if "O" not in tablero_barcos_jugador:
        print("¡Lo siento! Has perdido la partida")

    elif "O" not in tablero_barcos_maquina:
        print("¡Enhorabuena! Has ganado la partida")
            
'''
Definicion de funcion del juego que interactúa con el jugador
'''
def turnojugador(tablero_barcos_maquina, tablero_barcos_jugador, tablero_impactos_maquina, tablero_impactos_jugador):
    #Establece la condición de seguir ejecutando el bucle mientras hayan barcos en el tablero de ambos jugadores
    while "O" in tablero_barcos_maquina and "O" in tablero_barcos_jugador: 

        coord1 = (input("Introduce 1 coordenada del 0 al 9 por favor: "))
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
            
        letra = input("Introduce letra de la A la J, por favor: ")
        coord2 = cons.alfabeto[letra]
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
            print("¡Has acertado!")
            impacto.play()
            time.sleep(2)
            t.imprimir_tablero(tablero_impactos_maquina)
            continue
        elif tablero_barcos_maquina[coorden] == "-":
            tablero_barcos_maquina[coorden] = "-"
            tablero_impactos_maquina[coorden] = "-"
            print ("¡Has vuelto a dar en agua!")
            agua.play()
            time.sleep(2)
            t.imprimir_tablero(tablero_impactos_maquina)
            juegomaquina(tablero_barcos_jugador, tablero_barcos_maquina, tablero_impactos_jugador, tablero_impactos_maquina)
        
        elif tablero_barcos_maquina[coorden] == " ":
            tablero_barcos_maquina[coorden] = "-"
            tablero_impactos_maquina[coorden] = "-"
            print ("¡Has dado en agua!")
            agua.play()
            time.sleep(2)
            t.imprimir_tablero(tablero_impactos_maquina)
            juegomaquina(tablero_barcos_jugador, tablero_barcos_maquina, tablero_impactos_jugador, tablero_impactos_maquina)

       
    #Bucle que define el comportamiento de no haber barcos en algunos de los dos tableros: 
    if "O" not in tablero_barcos_jugador:
        print("¡Lo siento! Has perdido la partida")

    elif "O" not in tablero_barcos_maquina:
        print("¡Enhorabuena! Has ganado la partida")
   
