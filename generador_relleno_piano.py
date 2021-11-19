import random

def generarRellenoPiano(clave, subdivision_clave):
    factor = clave[0]
    reglon = []
    relleno = []
    repeticiones = len(clave)
    
    for i in range(0, factor):
        valor = random.randrange(0,3)
        reglon.append(valor)

    for i in range(0, repeticiones):
        for o in range(0, factor):
            relleno.append(reglon[o])
    return relleno
    