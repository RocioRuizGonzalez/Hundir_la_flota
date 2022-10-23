import numpy as np
import partida as p
import tableros as t
import bienvenida as b
import salida as s

'''
Iniciación del juego
'''
tablero_impactos_maquina = t.creartableros()

tablero_impactos_jugador = t.creartableros()

tablero_barcos_maquina = t.iniciar_tablero_con_barcos()
tablero_barcos_jugador = t.iniciar_tablero_con_barcos()

b.bienvenida()
t.imprimir_tablero(tablero_impactos_maquina)
p.turnojugador(tablero_barcos_maquina, tablero_barcos_jugador, tablero_impactos_maquina, tablero_impactos_jugador)
s.salir_del_juego(tablero_barcos_jugador, tablero_barcos_maquina)
