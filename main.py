############################################################################################
#                                            Main                                          #
############################################################################################

from generador_melodia import generarMelodia
from player import player
from generador_clave import generarClave
from generador_ritmo import generarRitmo
from generador_acordes import generarAcordes
from banda import banda


menu = '''------------------ Bienvenido al generador de musica procedural ------------------'''

print(menu)

clave = []

nota_clave = input("Ingrese la nota clave:")

acordes = generarAcordes(nota_clave)

escala = generarMelodia(nota_clave)


clave_input = input("Clave:\n1. 3/4.\n2 4/4.\nIngrese la clave: ")
if (clave_input == '1'):
    clave = [3, 4]
elif (clave_input == '2'):
    clave = [4, 4] 
tempo = int(input("Ingrese el tempo (bpm): "))

cantidad_subdivision, subdivision_base = generarRitmo(clave)

ritmo, piano, melodia, factor = generarClave(cantidad_subdivision, subdivision_base)

print(piano)
ritmo, subdivision_tiempo = player(ritmo, tempo, factor)


#0, 1, 2
#[0, 2, 0, 1, 1, 0, 2]


#ritmo2 = [[1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1], [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0]]

#do re mi fa sol la si
#1  2  3  4  5   6  7
#102039487382923098


banda(ritmo, piano, acordes, melodia, escala, subdivision_tiempo)
 




