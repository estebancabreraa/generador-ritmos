from generador_relleno import generarRelleno
from player import player
import random 

def generarClave(cantidad_subdivision, subdivision_base):
    multiplos = [1, 2, 4]
    factor = random.choice(multiplos)
    clave = []
    if factor == 1:
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

    hihat = generarRelleno(clave, subdivision_clave)
    snare = generarRelleno(clave, subdivision_clave)
    kick = generarRelleno(clave, subdivision_clave)

    ritmo = []

    ritmo.append(hihat)
    ritmo.append(snare)
    ritmo.append(kick)

    return ritmo, factor
