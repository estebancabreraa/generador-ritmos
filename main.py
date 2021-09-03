############################################################################################
#                                            Main                                          #
############################################################################################

from player import player
from generador_clave import generarClave
from generador_ritmo import generarRitmo
from bateria import bateria


menu = '''------------------ Bienvenido al generador de musica procedural ------------------'''

print(menu)

clave = []

clave_input = input("Clave:\n1. 3/4.\n2 4/4.\nIngrese la clave: ")
if (clave_input == '1'):
    clave = [3, 4]
elif (clave_input == '2'):
    clave = [4, 4] 
tempo = int(input("Ingrese el tempo (bpm): "))

cantidad_subdivision, subdivision_base = generarRitmo(clave)

ritmo, factor = generarClave(cantidad_subdivision, subdivision_base)

ritmo, subdivision_tiempo = player(ritmo, tempo, factor)

bateria(ritmo, subdivision_tiempo)
 




