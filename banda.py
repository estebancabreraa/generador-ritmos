from player import player
import time
from pygame import mixer 

def banda(ritmo, piano, acordes, melodia, escala, subdivision_tiempo):
    
    mixer.init()
    

    sonido_hihat = mixer.Sound('Samples/Drums/hihat.ogg')
    sonido_snare = mixer.Sound('Samples/Drums/snare.ogg')
    sonido_kick = mixer.Sound('Samples/Drums/kick.ogg')

    c = mixer.Sound('Samples/Piano/c.wav')
    cSharp = mixer.Sound('Samples/Piano/c#.wav')
    d = mixer.Sound('Samples/Piano/d.wav')
    dSharp = mixer.Sound('Samples/Piano/d#.wav')
    e = mixer.Sound('Samples/Piano/e.wav')
    f = mixer.Sound('Samples/Piano/f.wav')
    fSharp = mixer.Sound('Samples/Piano/f#.wav')
    g = mixer.Sound('Samples/Piano/g.wav')
    gSharp =  mixer.Sound('Samples/Piano/g#.wav')
    a = mixer.Sound('Samples/Piano/a.wav')
    aSharp = mixer.Sound('Samples/Piano/a#.wav')
    b = mixer.Sound('Samples/Piano/b.wav')


    cantidadNotas = len(ritmo[0])

    
    for i in range(0, cantidadNotas):
        if (ritmo[0][i] == 1):
            sonido_hihat.play()
        if (ritmo[1][i] == 1):
            sonido_snare.play()
        if (ritmo[2][i] == 1):
            sonido_kick.play()
        if acordes[piano[i]][0] == 'C' or acordes[piano[i]][1] == 'C' or acordes[piano[i]][2] == 'C':
            c.play()
        if acordes[piano[i]][0] == 'C#' or acordes[piano[i]][1] == 'C#' or acordes[piano[i]][2] == 'C#':
            cSharp.play()
        if acordes[piano[i]][0] == 'D' or acordes[piano[i]][1] == 'D' or acordes[piano[i]][2] == 'D':
            d.play()
        if acordes[piano[i]][0] == 'D#' or acordes[piano[i]][1] == 'D#' or acordes[piano[i]][2] == 'D#':
            dSharp.play()
        if acordes[piano[i]][0] == 'E' or acordes[piano[i]][1] == 'E' or acordes[piano[i]][2] == 'E':
            e.play()
        if acordes[piano[i]][0] == 'F' or acordes[piano[i]][1] == 'F' or acordes[piano[i]][2] == 'F':
            f.play()
        if acordes[piano[i]][0] == 'F#' or acordes[piano[i]][1] == 'F#' or acordes[piano[i]][2] == 'F#':
            fSharp.play()
        if acordes[piano[i]][0] == 'G' or acordes[piano[i]][1] == 'G' or acordes[piano[i]][2] == 'G':
            g.play()
        if acordes[piano[i]][0] == 'G#' or acordes[piano[i]][1] == 'G#' or acordes[piano[i]][2] == 'G#':
            gSharp.play()
        if acordes[piano[i]][0] == 'A' or acordes[piano[i]][1] == 'A' or acordes[piano[i]][2] == 'A':
            a.play()
        if acordes[piano[i]][0] == 'A#' or acordes[piano[i]][1] == 'A#' or acordes[piano[i]][2] == 'A#':
            aSharp.play()
        if acordes[piano[i]][0] == 'B' or acordes[piano[i]][1] == 'B' or acordes[piano[i]][2] == 'B':
            b.play()
        if escala[melodia[i]] == 'C':
            c.play()
        if escala[melodia[i]] == 'C#':
            cSharp.play()
        if escala[melodia[i]] == 'D':
            d.play()
        if escala[melodia[i]] == 'D#':
            dSharp.play()
        if escala[melodia[i]] == 'E':
            e.play()
        if escala[melodia[i]] == 'F':
            f.play()
        if escala[melodia[i]] == 'F#':
            fSharp.play()
        if escala[melodia[i]] == 'G':
            g.play()
        if escala[melodia[i]] == 'G#':
            gSharp.play()
        if escala[melodia[i]] == 'A':
            a.play()
        if escala[melodia[i]] == 'A#':
            aSharp.play()
        if escala[melodia[i]] == 'B':
            b.play()
            

        time.sleep(subdivision_tiempo/1000)





    
        