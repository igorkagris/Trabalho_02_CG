#

def rasterize_draw_area(vertices, viewport): #define y minimo e y maximo da figura
    ymin = vertices[0][1]
    v_ymin = 0
    for i in range (len(vertices)):
        if vertices[i][1] < ymin:
            ymin = vertices[i][1]
            v_ymin = i


    v_atual = v_ymin
    while 1:

        if v_atual == len(vertices)-1:
            v_prox = 0
        else:
            v_prox = v_atual + 1

        tx_x = (vertices[v_prox][0] - vertices[v_atual][0])/(vertices[v_prox][1] - vertices[v_atual][1])
        x = vertices[v_atual][0]
        scanline = []
        if vertices[v_atual][1] != vertices[v_prox][1]:
            for y in range(vertices[v_atual][1], vertices[v_prox][1]):
                x = x+tx_x
                if (len(scanline)-1 < y-ymin):
                    scanline.append([x]) #Se a linha ainda não foi criada, cria um vetor na linha Y[1] = [x]
                else:                          
                    scanline[y-ymin].append(x) #Se a linha já foi criada adiciona apenas mais um valor no vetor Y1[1] = [x, x2]
        vertices[i]
        vertices[i+1]


        if v_prox+1 == v_ymin:
            break

    return scanline #Retorna uma lista com y pares de pontos x de inicio e fim de cada linha a ser rasterizada na tela