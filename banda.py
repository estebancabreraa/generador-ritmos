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
        print("--------------Conjunto--------------")
        if (ritmo[0][i] == 1):
            sonido_hihat.play()
        if (ritmo[1][i] == 1):
            sonido_snare.play()
        if (ritmo[2][i] == 1):
            sonido_kick.play()
        if acordes[piano[i]][0] == 'C':
            print("Acorde: C")
        if acordes[piano[i]][0] == 'C#':
            print("Acorde: C#")
        if acordes[piano[i]][0] == 'D':
            print("Acorde: D")
        if acordes[piano[i]][0] == 'D#':
            print("Acorde: D#")
        if acordes[piano[i]][0] == 'E':
            print("Acorde: E")
        if acordes[piano[i]][0] == 'F':
            print("Acorde: F")
        if acordes[piano[i]][0] == 'F#':
            print("Acorde: F#")
        if acordes[piano[i]][0] == 'G':
            print("Acorde: G")
        if acordes[piano[i]][0] == 'G#':
            print("Acorde: G#")
        if acordes[piano[i]][0] == 'A':
            print("Acorde: A")
        if acordes[piano[i]][0] == 'A#':
            print("Acorde: A#")
        if acordes[piano[i]][0] == 'B':
            print("Acorde: B")
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
            print("Nota melodia: C")
        if escala[melodia[i]] == 'C#':
            cSharp.play()
            print("Nota melodia: C#")
        if escala[melodia[i]] == 'D':
            d.play()
            print("Nota melodia: D")
        if escala[melodia[i]] == 'D#':
            dSharp.play()
            print("Nota melodia: D#")
        if escala[melodia[i]] == 'E':
            e.play()
            print("Nota melodia: E#")
        if escala[melodia[i]] == 'F':
            f.play()
            print("Nota melodia: F")
        if escala[melodia[i]] == 'F#':
            fSharp.play()
            print("Nota melodia: F#")
        if escala[melodia[i]] == 'G':
            g.play()
            print("Nota melodia: G")
        if escala[melodia[i]] == 'G#':
            gSharp.play()
            print("Nota melodia: G#")
        if escala[melodia[i]] == 'A':
            a.play()
            print("Nota melodia: A")
        if escala[melodia[i]] == 'A#':
            aSharp.play()
            print("Nota melodia: A#")
        if escala[melodia[i]] == 'B':
            b.play()
            print("Nota melodia: B")
            

        time.sleep(subdivision_tiempo/1000)





    
        