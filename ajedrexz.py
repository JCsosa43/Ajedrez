
from PIL import Image

class Piezas:
    def __init__(self, nombre, color, posicion, imagen_path):
        self.nombre = nombre
        self.color = color
        self.posicion = posicion
        self.imagen_path = imagen_path
        self.imagen = Image.open(imagen_path)
        
        
class Reina (Piezas):
    def __init__(self, nombre, color, posicion):
        super().__init__(nombre, color, posicion)


    def mostrar_imagen(self):
        self.imagen.show()