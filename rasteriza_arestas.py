
def v_ant_prox(v, vs): #retorna o vertice anterior e o proximo
    if v == len(vs)-1: #Se o vertice atual for o ultimo, o proximo é o primeiro
        return v-1, 0
    elif v == 0: #Se o vertice atual for o primeiro, o anterior é o ultimo
        return len(vs)-1, v+1
    else:
        return v-1, v+1

def incrementando(v1, v2): #retorna 1 se está incrementando e -1 decrementando
    if v1 < v2:
        return 1
    return -1

def y_min(v):   #retorna y minimo e sua posição
    ymin = v[0][1]
    v_ymin = 0
    for i in range (len(v)):
        if v[i][1] < ymin:
            ymin = v[i][1]
            v_ymin = i
    return ymin, v_ymin

'''
A função retora um vetor com pares iniciais e finais de uma linha a ser rasterizada na tela
válido pra qualquer objeto, logo:
 - arestas horizontais tem x inicial e final com valores diferentes, sem passar pelo processamento
 - Arestas não horizontais:
    - Linhas que contém vértice de pico superior ou inferior tem x inicial e final com mesmo valor
    - Arestas passam pelo processamento de Y inicial+1 a Y final-1, propagando tx
 - Arestas horizontais (e que não são pico) não estão tratadas. Logo haverá um caso onde o vetor contém 3 valores
'''
def rasterize_draw_area(vertices): #define y minimo e y maximo da figura

    ymin, v_ymin = y_min(vertices)

    v_atual = v_ymin
    scanline = []
    while 1:
        

        v_ant, v_prox = v_ant_prox(v_atual, vertices)
        


        x = vertices[v_atual][0] # x inicial
        
        if vertices[v_atual][1] != vertices[v_prox][1]: #Aresta não horizontal

            #propaga uma taxa negativa para quando X prox < X atual e positiva quando X atual < X prox.
            tx_x = (vertices[v_prox][0] - vertices[v_atual][0])/abs(vertices[v_prox][1] - vertices[v_atual][1])


            if ((vertices[v_ant][1]<vertices[v_atual][1]) and (vertices[v_atual][1]>vertices[v_prox][1]))  or ((vertices[v_ant][1]>vertices[v_atual][1]) and (vertices[v_atual][1]<vertices[v_prox][1])):
                if (len(scanline)-1 < vertices[v_atual][1]-ymin):   # pico superior/\ ou inferior\/ insere x inicial e final na mesma linha
                    scanline.append([(int(x)), (int(x))]) 
                else:
                    scanline[vertices[v_atual][1]-ymin].append((int(x)))
                    scanline[vertices[v_atual][1]-ymin].append((int(x)))
            else:
                if (len(scanline)-1 < vertices[v_atual][1]-ymin):
                    scanline.append([(int(x))])
                else:
                    scanline[vertices[v_atual][1]-ymin].append((int(x)))

            x = x+tx_x
            
            i = incrementando(vertices[v_atual][1], vertices[v_prox][1])
            for y in range(vertices[v_atual][1]+i, vertices[v_prox][1], +i):
                    
                if (len(scanline)-1 < y-ymin): #Se linha não criada, cria vetor linha Y[1] = [x]
                    scanline.append([(int(x))])    #Como o primeiro vertice é o menor y, a primeira aresta é sempre descendo
                else:                          
                    scanline[y-ymin].append((int(x))) #Se a linha já foi criada adiciona apenas mais um valor no vetor Y1[1] = [x, x2]

                x = x+tx_x

        else: #Aresta horizontal
            if (len(scanline)-1 < vertices[v_atual][1]-ymin): #Se linha não criada, cria vetor linha Y[1] = [x]
                scanline.append([(int(x))]) #x inicial e final na mesma linha
            else:
                scanline[vertices[v_atual][1]-ymin].append((int(x)))


        v_atual = v_prox

        if v_atual == v_ymin:
            break

    return scanline #Retorna uma lista com y pares de pontos x de inicio e fim de cada linha a ser rasterizada na tela

''' TESTE com falha
vertices = [(10, 1), (1, 5), (3, 5), (10, 10), (5, 10)]

scanlines = rasterize_draw_area(vertices)

print (scanlines)  

'''
''' EXEMPLO DA FALHA
     /\ 
    /  \ 
   /    \ 
  /_     \ 
    \    /
     \  /
      \/
'''