from math import inf as infinity
from random import choice
import platform
import time
from os import system
import Table


jugador= -1
JugadorIA = +1


def clean():
    """
    Limpia la consola
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def evaluar(tablero):

    if ganar(tablero, JugadorIA):
        puntaje = +1
    elif ganar(tablero, jugador):
        puntaje = -1
    else:
        puntaje = 0

    return puntaje


def miniMax(tablero, profundidad, jugador):
    matriz = tablero.getTablero()
    if jugador == JugadorIA:
        mejor = [-1, -1, -infinity]
    else:
        mejor = [-1, -1, infinity]

    if profundidad == 0 or finJuego(tablero):
        puntaje = evaluar(tablero)
        return [-1, -1, puntaje]

    for c in celdas_vacias(tablero):
        x, y = c[0], c[1]
        matriz[x][y] = jugador
        puntaje= miniMax(tablero, profundidad - 1, -jugador)
        matriz[x][y] = 0
        puntaje[0], puntaje[1] = x, y

        if jugador == JugadorIA:
            if puntaje[2] > mejor[2]:
                mejor = puntaje
        else:
            if puntaje[2] < mejor[2]:
                mejor = puntaje

    return mejor


def finJuego(tablero):
    matriz = tablero.getTablero()
    return ganar(tablero, jugador) or ganar(tablero, JugadorIA)


def ganar(tablero, jugador):
    matriz = tablero.getTablero()
    win_state = [
        [matriz[0][0], matriz[0][1], matriz[0][2]],
        [matriz[1][0], matriz[1][1], matriz[1][2]],
        [matriz[2][0], matriz[2][1], matriz[2][2]],
        [matriz[0][0], matriz[1][0], matriz[2][0]],
        [matriz[0][1], matriz[1][1], matriz[2][1]],
        [matriz[0][2], matriz[1][2], matriz[2][2]],
        [matriz[0][0], matriz[1][1], matriz[2][2]],
        [matriz[2][0], matriz[1][1], matriz[0][2]],
    ]
    if [jugador, jugador, jugador] in win_state:
        return True
    else:
        return False


def validarMovimiento(x, y, tablero):
    matriz= tablero.getTablero()
    if [x, y] in celdas_vacias(tablero):
        return True
    else:
        return False


def establecerMovimiento(x, y, jugador, tablero):
    matriz= tablero.getTablero()
    if validarMovimiento(x, y, tablero):
        matriz[x][y] = jugador
        tablero.setTablero(matriz)
        return True
    else:
        return False


def celdas_vacias(tablero):
    matriz = tablero.getTablero()
    celdas = []
    for x, fila in enumerate(matriz):
        for y, col in enumerate(fila):
            if col == 0:
                celdas.append([x, y])

    return celdas


def imprimirTablero(tablero, fichaJugador, fichaIA):
    vacio= ""
    fichas = {
        -1: fichaJugador,
        +1: fichaIA,
        0: vacio
    }
    matriz= tablero.getTablero()
    lineaString = "-------------"

    print("\n" + lineaString)
    for f in matriz:
        for c in f:
            simbolo = fichas[c]
            print(f"| {simbolo} |", end="")
        print("\n" + lineaString)


def aiTurno(fichaJugador, fichaIA, tablero):
    matriz = tablero.getTablero()
    profundidad = len(celdas_vacias(tablero))
    if profundidad == 0 or finJuego(tablero):
        return

    clean()
    print(f"IA turno [{fichaIA}]")
    imprimirTablero(tablero, fichaJugador, fichaIA)

    if profundidad == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        movimiento = miniMax(tablero, profundidad, JugadorIA)
        x, y = movimiento[0], movimiento[1]

    establecerMovimiento(x, y, fichaIA, tablero)
    time.sleep(1)


def jugadorTurno(fichaJugador, fichaIA, tablero):
    matriz = tablero.getTablero()
    profundidad = len(celdas_vacias(tablero))
    if profundidad == 0 or finJuego(tablero):
        return

    movimiento = -1
    movimientosPosibles = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f"Turno del jugador [{fichaJugador}]")
    imprimirTablero(tablero, fichaJugador, fichaIA)

    while movimiento < 1 or movimiento > 9:
        try:
            movimiento = int(input('Use numpad (1..9): '))
            coordenada = movimientosPosibles[movimiento]
            posible = establecerMovimiento(coordenada[0], coordenada[1], jugador, tablero)

            if not posible:
                print('Bad move')
                move = -1
        except (KeyError, ValueError):
            print('Error, elija de nuevo su movimiento')

def main():
    clean()

    tablero = Table.tablero()
    tablero.inicializarTablero()
    jugador, ia = tablero.elegirFicha()
    if tablero.turno():
        jugadorTurno(jugador, ia, tablero)

    while len(celdas_vacias(tablero)) > 0 and not finJuego(tablero):
        aiTurno(jugador, ia, tablero)
        jugadorTurno(jugador, ia, tablero)

    if ganar(tablero, jugador):
        clean()
        print(f"Turno del jugador [{jugador}]")
        imprimirTablero(tablero, jugador, ia)
        print("GANASTE!")
    elif ganar(tablero, JugadorIA):
        clean()
        print(f"Turno de IA [{ia}]")
        imprimirTablero(tablero, jugador, ia)
        print("Perdiste")
    else:
        clean()
        imprimirTablero(tablero, jugador, ia)
        print("Empate")

    exit()


if __name__ == '__main__':
    main()
