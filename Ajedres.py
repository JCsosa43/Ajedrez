

class Piezas:
    def __init__(self, nombre, color, posicion):
        self.nombre = nombre
        self.color = color
        self.posicion = posicion
        
        
class Reina (Piezas):
    def __init__(self, nombre, color, posicion):
        super().__init__(nombre, color, posicion)
        
class Rey (Piezas):
    def __init__(self, nombre, color, posicion):
        super().__init__(nombre, color, posicion)
        
class Torre (Piezas):
    def __init__(self, nombre, color, posicion):
        super().__init__(nombre, color, posicion)
        
class Alfil (Piezas):
    def __init__(self, nombre, color, posicion):
        super().__init__(nombre, color, posicion)
        
class Caballo (Piezas):
    def __init__(self, nombre, color, posicion):
        super().__init__(nombre, color, posicion)
        
class Peon (Piezas):
    def __init__(self, nombre, color, posicion):
        super().__init__(nombre, color, posicion)
        