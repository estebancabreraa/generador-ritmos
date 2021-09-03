############################################################################################
#                                            Main                                          #
############################################################################################

menu = '''------------------ Bienvenido al generador de musica procedural ------------------'''

print(menu)

clave = input("Clave:\n1. 3/4.\n2 4/4.\nIngrese la clave: ")
if (clave == 1):
    clave = '3/4'
elif (clave == 2):
    clave = '4/4'
tempo = input("Ingrese el tempo (bpm): ")

