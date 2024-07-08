from Piezas import Piezas

class Torre (Piezas):
    def __init__(self, nombre, color, posicion):
        super().__init__(nombre, color, posicion)
        
    def movimiento(self, movimiento_col, movimiento_fila):
        if movimiento_col.upper() != self.posicion[0] and movimiento_fila != self.posicion[1]: #(SP) Validacion que el usuario no se realice un movimiento en diagonal.
            print("Movimiento incorrecto. Movimiento en diagonal no permitido")
        else: 
            self.posicion = [movimiento_col.upper(), movimiento_fila]
            print (f"El {self.nombre} {self.color} esta en la posicion: {self.posicion[0]}{self.posicion[1]}")
            
            