import random

def generarRelleno(clave, subdivision_clave):
    factor = clave[0]
    reglon = []
    relleno = []
    repeticiones = len(clave)
    
    '''for i in range(0, repeticiones):
        for i in range(0, factor):
            valor = random.randrange(0,2)
            reglon.append(valor)
        for o in range(0, factor):
            relleno.append(reglon[o])
    return relleno'''
    
def generarRelleno(clave, subdivision_clave):
    factor = clave[0]
    reglon = []
    relleno = []
    for i in range(0, factor):
        valor = random.randrange(0,2)
        reglon.append(valor)
    repeticiones = len(clave)

    for i in range(0, repeticiones):
        for o in range(0, factor):
            relleno.append(reglon[o])
    return relleno