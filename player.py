def player(ritmo, tempo, factor):
    subdivision_tiempo = (60/tempo)/factor * 1000 # milisegundos
    return ritmo, subdivision_tiempo

