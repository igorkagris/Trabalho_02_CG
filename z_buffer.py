#Válido apenas para polígonos convexos
def rasterize_draw_area(vertices): #define y minimo e y maximo da figura
    ymin = vertices[0][1]
    v_ymin = 0
    for i in range (len(vertices)):
        if vertices[i][1] < ymin:
            ymin = vertices[i][1]
            v_ymin = i

    scanline = []
    v_atual = v_ymin
    aux = 2
    while 1:

        if v_atual == len(vertices)-1:
            v_prox = 0
        else:
            v_prox = v_atual + 1
                                        #propaga uma taxa negativa quando x1 < x0.
        tx_x = (vertices[v_prox][0] - vertices[v_atual][0])/(vertices[v_prox][1] - vertices[v_atual][1])

        x = vertices[v_atual][0] # x inicial
        if vertices[v_atual][1] != vertices[v_prox][1]: #Aresta não horizontal
            
            if vertices[v_atual][1] > vertices[v_prox][1]: # aresta está subindo
                if aux == 1 or aux == 2:
                    y = vertices[v_atual][1]        # y inicial p/ pico
                else:
                    y = vertices[v_atual][1]            # y inicial
                aux = -1                            # decremento de y
                tx_x = -tx_x                        # inverte também a tx de x 
            else:
                if aux == -1 or aux == 2:
                    y = vertices[v_atual][1]        # y inicial p/ pico
                else:
                    y = vertices[v_atual][1]    #descendo
                aux = 1            # y inicial

            while y != vertices[v_prox][1]:
                if (len(scanline)-1 < y-ymin):      #Se linha não criada, cria vetor linha Y[1] = [x]
                    scanline.append([(int(x))])     #Como o primeiro vertice é o menor y, a primeira aresta é sempre descendo
                else:                          
                    scanline[y-ymin].append((int(x))) #Se a linha já foi criada adiciona apenas mais um valor no vetor Y1[1] = [x, x2]
                x = x+tx_x
                y = y + aux

        v_atual = v_prox

        if v_atual == v_ymin:
            break

    return scanline #Retorna uma lista com y pares de pontos x de inicio e fim de cada linha a ser rasterizada na tela

def rasterizar_vertices(vertices):
    ordered_vertices = sorted(vertices, key=lambda v: v[1]) # Ordena o vértices crescente em y

    y_min = ordered_vertices[0][1]
    y_max = ordered_vertices[-1][1]


    bordas_esquerda = []   #Lista para armazenar x para cada y
    bordas_direita = []

   
    for i in range(len(ordered_vertices)+1):      # Calcular as bordas esquerda e direita para cada linha

        x1, y1 = ordered_vertices[i]
        if (i == len(ordered_vertices)): 
            x2, y2 = ordered_vertices[0]
        x2, y2 = ordered_vertices[i + 1]

        if y1 != y2:  #Linha não horizontal
            tx = (x2 - x1) / (y2 - y1) # Calcular tx de x p cada y

            for y in range (y2-y1):  # Percorrer cada linha entre y1 e y2
                x += tx
                bordas_esquerda[y] = min(bordas_esquerda[i], int(x))
                bordas_direita[y] = max(bordas_direita[i], int(x))

    # Pintar pixel a pixel
    for y in range(y_min, y_max + 1):
        for x in range(bordas_esquerda[y - y_min], bordas_direita[y - y_min] + 1):
            # Pintar o pixel (x, y)
            print(f"Pintando pixel ({x}, {y})")

# Exemplo de uso com um polígono de 4 lados:
vertices = [(1, 5), (3, 2), (7, 6), (5, 8)]

scanlines = rasterize_draw_area(vertices)

print (scanlines)