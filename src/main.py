import numpy as np
import partida as p
import tableros as t
import bienvenida as b

'''
Iniciación del juego
'''
tablero_impactos_maquina = t.creartableros()
t.imprimir_tablero(tablero_impactos_maquina)

tablero_impactos_jugador = t.creartableros()
t.imprimir_tablero(tablero_impactos_jugador)

tablero_barcos_maquina = t.iniciar_tablero_con_barcos()
tablero_barcos_jugador = t.iniciar_tablero_con_barcos()
t.imprimir_tablero(tablero_barcos_maquina)
t.imprimir_tablero(tablero_barcos_jugador)

b.bienvenida()
p.turnojugador(tablero_barcos_maquina, tablero_barcos_jugador, tablero_impactos_maquina, tablero_impactos_jugador)
