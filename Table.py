from miniMax_v2 import clean


class tablero:
    tablero = 0
    def inicializarTablero(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0],]
        return tablero

    def getTablero(self):
        return self.tablero

    def setTablero(self, matriz):
        self.tablero = matriz

    def elegirFicha(self):
        jugador = ""
        ia = ""
        while jugador != 'O' and jugador != 'X':
            jugador = input("Elija X o O\nElegir: ").upper()
            while jugador != "O" and jugador != "X":
                print("Error, elegir bien su opcion")
                jugador = input("Elija X o O\nElegir: ").upper()

        if jugador == "X":
            ia = "O"
        else:
            ia = "X"

        clean()

        return jugador, ia

    def turno(self):
        primero= 0
        while primero != "Y" and primero != "N":
            primero = input("Quiere ser el primero en empezar?[y/n]: ").upper()
            while primero != "Y" and primero != "N":
                print("Error, elegir la opcion correcta")
                primero = input("Quiere ser el primero en empezar?[y/n]: ").upper()

        if primero == "Y":
            return True
        else:
            return False

    def jugarHumano(self, f, c, jugador):
        if f < 3 and c < 3:
            self.tablero[f][c] = jugador
            return True
        else:
            return False
