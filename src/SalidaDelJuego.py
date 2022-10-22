'''
Función de salida del Juego. Cuando todos los barcos hayan sido hundidos se termina el juego.
'''

def salir_del_juego():
    
    if tablerobarcos_jugador != "0":
        print(f"Ohhh has perdido esta batalla {nombre_jugador}")
        game_over = True
    elif tablerobarcos_maquina != "0":
        print(f"¡Has Ganado {nombre_jugador}!")
        game_over = True