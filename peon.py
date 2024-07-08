from Piezas import Piezas

class Peon (Piezas):
    def __init__(self, nombre, color, posicion):
        super().__init__(nombre, color, posicion)

    def movimiento(self, movimiento_col, movimiento_fila):
        mover_filas = int(movimiento_fila)-int(self.posicion[1]) #Saber cuantas filas se intenta mover el usuario, sacando la diferencia entre la fila final y la fila inicial
        if movimiento_col.upper() == self.posicion[0] and mover_filas == 1: #Regla de juego: Que la pieza permanezca en la misma columna y se mueva una casilla a la vez.
            self.posicion = [movimiento_col.upper(), movimiento_fila]
            print (f"El {self.nombre} {self.color} esta en la posicion: {self.posicion[0]}{self.posicion[1]}\n")
        
        else:
            print("Movimiento incorrecto. Solo se puede mover una casilla por turno")