############################################################################################
#                                            Main                                          #
############################################################################################

from generador_melodia import generarMelodia
from player import player
from generador_clave import generarClave
from generador_ritmo import generarRitmo
from generador_acordes import generarAcordes
from generador_formas import generarForma
from banda import banda


menu = '''------------------ Bienvenido al generador de musica procedural ------------------'''

print(menu)

clave = []

nota_clave = input("Ingrese la nota clave:")

acordes = generarAcordes(nota_clave)

escala = generarMelodia(nota_clave)

forma = generarForma()


clave_input = input("Clave:\n1. 3/4.\n2 4/4.\nIngrese la clave: ")
if (clave_input == '1'):
    clave = [3, 4]
elif (clave_input == '2'):
    clave = [4, 4] 
tempo = int(input("Ingrese el tempo (bpm): "))

#VERSO

cantidad_subdivision, subdivision_base = generarRitmo(clave)

ritmoVerso, pianoVerso, melodiaVerso, factor = generarClave(cantidad_subdivision, subdivision_base)

print(melodiaVerso)
ritmoVerso, subdivision_tiempo = player(ritmoVerso, tempo, factor)

#PUENTE

cantidad_subdivision, subdivision_base = generarRitmo(clave)

ritmoPuente, pianoPuente, melodiaPuente, factor = generarClave(cantidad_subdivision, subdivision_base)

print(melodiaPuente)
ritmoPuente, subdivision_tiempo = player(ritmoPuente, tempo, factor)

#CORO

cantidad_subdivision, subdivision_base = generarRitmo(clave)

ritmoCoro, pianoCoro, melodiaCoro, factor = generarClave(cantidad_subdivision, subdivision_base)

print(melodiaPuente)
ritmoCoro, subdivision_tiempo = player(ritmoCoro, tempo, factor)

for i in range(0, len(forma)):
    for o in range (0, len(forma[i])):
        if (forma[i][o] == 'v'):
            banda(ritmoVerso, pianoVerso, acordes, melodiaVerso, escala, subdivision_tiempo)
        if (forma[i][o] == 'p'):
            banda(ritmoPuente, pianoPuente, acordes, melodiaPuente, escala, subdivision_tiempo)
        if (forma[i][o] == 'c'):
            banda(ritmoCoro, pianoCoro, acordes, melodiaCoro, escala, subdivision_tiempo)
 




