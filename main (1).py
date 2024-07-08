from Piezas import *
from Peon import *
from Reina import *
from Caballo import *
from Alfil import *
from Rey import *
from Torre import *

def main():
    peon1 = Peon ("Peon-1", "Negro",["A","7"])
    print (f"El {peon1.nombre} {peon1.color} esta en la posicion: {peon1.posicion[0]}{peon1.posicion[1]}")
    print("Ingrese el siguiente movimiento: Ejemplo: A2, A3, etc...\n")
    movimiento_col = input("Ingresa la columna: Letra\n")
    movimiento_fila = input("Ingresa la fila: Numero\n")
    
    peon1.movimiento(movimiento_col, movimiento_fila)
    
    
    torre1 = Torre ("Torre-1", "Negro",["A","8"])
    print (f"El {torre1.nombre} {torre1.color} esta en la posicion: {torre1.posicion[0]}{torre1.posicion[1]}")
    print("Ingrese el siguiente movimiento: Ejemplo: A7, A9, B8, etc...\n")
    movimiento_col = input("Ingresa la columna: Letra\n")
    movimiento_fila = input("Ingresa la fila: Numero\n")
    
    torre1.movimiento(movimiento_col, movimiento_fila)
 
    
if __name__ == "__main__":
    main()