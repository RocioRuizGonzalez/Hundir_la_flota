import numpy as np
import partida as p
import tableros as t

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

coorden = p.iniciarjuego()
print(coorden)

jugador1 = p.turnojugador(tablero_barcos_maquina, tablero_impactos_maquina, coorden)

coordenadas_maquina = p.coord_maquina()
print(coordenadas_maquina)
turnomaquina = p.turnomaquina(tablero_barcos_jugador, tablero_impactos_jugador, coordenadas_maquina)