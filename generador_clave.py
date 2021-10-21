from generador_relleno import generarRelleno
from generador_relleno_piano import generarRellenoPiano
from generador_relleno_melodia import generarRellenoMelodia
from player import player
import random 
import time

def generarClave(cantidad_subdivision, subdivision_base):
    multiplos = [1, 2, 4]
    factor = random.choice(multiplos)
    clave = []
    if factor == 1: #cambiar las posibles combinaciones.
        for i in range(0, cantidad_subdivision):
            clave.append(factor)
    else:
        opcion = random.randrange(0, 2)
        if opcion == 1: 
            for i in range(0, cantidad_subdivision):
                clave.append(factor)
        else:
            for i in range(0, factor):
                clave.append(cantidad_subdivision)

    subdivision_clave = factor * subdivision_base

    melodia = generarRellenoMelodia(clave, subdivision_clave)
    piano = generarRellenoPiano(clave, subdivision_clave)

    hihat = generarRelleno(clave, subdivision_clave)
    snare = generarRelleno(clave, subdivision_clave)
    while (snare == hihat):
        snare = generarRelleno(clave, subdivision_clave)
    kick = generarRelleno(clave, subdivision_clave)
    while ((snare == kick)):
        kick = generarRelleno(clave, subdivision_clave)

    ritmo = []

    ritmo.append(hihat)
    ritmo.append(snare)
    ritmo.append(kick)
    
    print(ritmo)

    return ritmo, piano, melodia, factor
