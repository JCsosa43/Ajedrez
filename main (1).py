from piezas import *
from peon import *
from reina import *
from caballo import *
from alfil import *
from rey import *
from torre import *

def main():
    rey1 = Rey ("Rey", "Negro","D1")
    print (rey1.nombre, rey1.color, rey1.posicion)

if __name__ == "__main__":
    main()