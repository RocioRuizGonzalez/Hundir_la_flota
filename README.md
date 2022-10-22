# Hundir la flota
## Descripción
Juego desarrollado en 5 scripts: bienvenida, constants, partida, tableros y main a través de lenguaje python.
### Desarrollo
Para iniciar el programa de juego hemos creado una bienvenida donde se saluda al usuario (jugador) y le presenta a su contrincante (la máquina-Popeye). 
A continuación hemos creado cuatro tableros, 2 con la función **tablero_barcos_maquina ** y **tablero_barcos_jugador**  (para tableros vacíos donde se van a ir reflejando los impactos) y otros 2 tableros con la función **iniciar_tablero_con_barcos** donde se colocarán los barcos de forma aleatoria (del jugador y de la máquina). 
Una vez que ya tenemos los barcos colocados en los tableros, iniciamos el juego con la función **iniciarjuego**. Aquí el jugador debe de ir introduciendo unas coordenadas de número y letra que serán los disparos en el tablero. 
Con la función **turnojugador** si  las coordenadas coincide con una parte de alguno de los barcos colocados aleatoriamente, se introducirá un simbolo *X*. En caso contrario, si lo que toca es agua, el simbolo que aparecerá será *-*. 
Si el jugador toca alguna de las partes del barco, repite turno, en caso contrario, es el turno de la máquina a través de la función **turnomaquina**
El juego termina cuando el jugador toca todos los barcos de la máquina o bien cuando la máquina toca todos los barcos del jugador. También puede terminar si el jugador voluntariamente decide aplicar la función **salida**.
#### Librerías usadas
* Numpy
* Random
* Time
#### Autores
* Génesis Rojas
* Javier López
* Antonio Ambrosio
* Rocío Ruiz