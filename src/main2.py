import numpy as np
import partida2 as p
import tableros as t
import bienvenida as b
import salida as s 
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
s.salir_del_juego(tablero_barcos_jugador, tablero_barcos_maquina)