'''
Definir funcion para poder visualizar tableros con letras como encabezado
'''


def imprimir_tablero(tablero):
        i = 0
        print("  A B C D E F G H I J")
        for fila in tablero:
               linea_imprimir = str(i) + " " 
               for elemento in fila:
                       linea_imprimir = linea_imprimir + elemento + " "
               print(linea_imprimir)
               i = i + 1