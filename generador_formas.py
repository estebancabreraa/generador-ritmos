import random

def generarForma():
    formas = []
    estructura = []
    puente = False
    
    valor = random.randrange(0,1)
    totalRepeticiones = random.randrange(3, 6)

    if (valor == 0):
        puente = True
        puenteRepeticiones = random.randrange(1,2)
    

    versoRepeticiones = random.randrange(1, 3)
    coroRepeticiones = random.randrange(1, 3)

    for i in range(0, versoRepeticiones):
        estructura.append('v')
    
    if (puente):
        for i in range(0, puenteRepeticiones):
            estructura.append('p')

    for i in range(0, coroRepeticiones):
        estructura.append('c')

    for i in range(0, totalRepeticiones):
        formas.append(estructura)
    
    print(formas)

    return formas

generarForma()

