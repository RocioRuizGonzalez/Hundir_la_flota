'''
Función de salida del Juego. Cuando todos los barcos hayan sido hundidos se termina el juego.
'''
import partida as p

def salir_del_juego(tablero_barcos_jugador, tablero_barcos_maquina):
    
    if "O" not in tablero_barcos_jugador:
        print("Ohhh has perdido esta batalla...")
    elif "O" not in tablero_barcos_maquina:
        print("¡Has Ganado!")
       