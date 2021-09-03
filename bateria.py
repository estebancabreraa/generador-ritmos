from player import player
import time
from pygame import mixer 

def bateria(ritmo, subdivision_tiempo):
    
    mixer.init()

    '''canal_hihat = mixer.Channel(0)
    canal_snare = mixer.Channel(1)
    canal_kick = mixer.Channel(2)'''

    sonido_hihat = mixer.Sound('Samples/Drums/hihat.ogg')
    sonido_snare = mixer.Sound('Samples/Drums/snare.ogg')
    sonido_kick = mixer.Sound('Samples/Drums/kick.ogg')

    sonido_hihat.play()
    sonido_snare.play()
    sonido_kick.play()
    
    #mixer.music.play(sonido_hihat)

    #canal_hihat.play(sonido_hihat, 1)
    #canal_snare.play(sonido_snare)
    #canal_kick.play(sonido_kick)

    #cantidad_notas = len(ritmo[0])


    
        