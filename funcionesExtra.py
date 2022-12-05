from os import system
import platform


def imprimirTablero(tablero, fichaJugador, fichaIA):
    vacio = ""
    fichas = {
        -1: fichaJugador,
        +1: fichaIA,
        0: vacio
    }
    matriz = tablero.getTablero()
    lineaString = "-------------"

    print("\n" + lineaString)
    for f in matriz:
        for c in f:
            simbolo = fichas[c]
            print(f"| {simbolo} |", end="")
        print("\n" + lineaString)


def celdas_vacias(tablero):
    matriz = tablero.getTablero()
    celdas = []
    for x, fila in enumerate(matriz):
        for y, col in enumerate(fila):
            if col == 0:
                celdas.append([x, y])

    return celdas


def validarMovimiento(x, y, tablero):
    # matriz= tablero.getTablero()
    if [x, y] in celdas_vacias(tablero):
        return True
    else:
        return False


def clean():
    """
    Limpia la consola, ponele
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')
