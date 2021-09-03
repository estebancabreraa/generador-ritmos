from player import player
import time
from pygame import mixer 

def bateria(ritmo, subdivision_tiempo):
    
    mixer.init()
    

    sonido_hihat = mixer.Sound('Samples/Drums/hihat.ogg')
    sonido_snare = mixer.Sound('Samples/Drums/snare.ogg')
    sonido_kick = mixer.Sound('Samples/Drums/kick.ogg')

    cantidadNotas = len(ritmo[0])

    while True:
        for i in range(0, cantidadNotas):
            if (ritmo[0][i] == 1):
                sonido_hihat.play()
            if (ritmo[1][i] == 1):
                sonido_snare.play()
            if (ritmo[2][i] == 1):
                sonido_kick.play()
            time.sleep(subdivision_tiempo/1000)





    
        