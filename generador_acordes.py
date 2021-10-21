def generarAcordes(notaUsuario):
    notas = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    index = 0
    index2 = 0
    for nota in notas:
        if (nota == notaUsuario):
            break
        index = index + 1
    
    index2 = index

    escala = []

    escala.append(notas[index%12])
    for i in range(0, 6):
        if (i == 2):
            index = index + 1
        elif (i == 6):
            index = index + 1
        else:
            index = index + 2
        escala.append(notas[index%12])

    acordes = []
    triadas = []
    for i in range(0, 7):
        if i == 0 or i == 3 or i == 4:
            index = notas.index(escala[i])
            triadas.append(notas[index%12])
            triadas.append(notas[(index + 4)%12])
            triadas.append(notas[(index + 7)%12])
            acordes.append(triadas)
            triadas = []
    print(acordes[2][2])
    return acordes 








    


    
    
              
    
        
        
        
