from generador_clave import generarClave

def generarRitmo(clave):
    cantidad_subdivision = int(clave[0])
    subdivision_base = int(clave[2])
    return cantidad_subdivision, subdivision_base

