        # Apenas para poligonos convexos

''' Começa pelo Ymin
    Lê as arestas 1 a 1, armazenando todas as coordenadas xy para cada y
    ao chegar no Ymax
    reinicia o processo, dessa vez separando os pontos em bordas esquerda e direita'''

#def transf_to_raster(obj, faces)

def vertice_raster(face):
    Ymin, Ymax = face[0][1], face[0][1]
    for a in face:               #descobre Ymin e Ymax da face
        Ymin = min(a[1], Ymin)
        Ymax = max(a[1], Ymax)

    bordas_esquerda = [float('inf')] * ((Ymax - Ymin + 1))  #Lista para armazenar x para cada y
    bordas_direita = [float('inf')] * ((Ymax - Ymin + 1))

    for i in range(len(face)):  #Calcula as bordas esquerda e direita para cada linha (y)
        x1, y1 = face[i]
        if i == len(face)-1:
            x2, y2 = face[0]
        else:
            x2, y2 = face[i+1]

        if y1 != y2:            #Linha não horizontal
            tx = abs((x2 - x1) / (y2 - y1))
            if x1 < x2:
                x = x1
            else:
                x = x2
            for y in range(min(y1, y2), max(y1, y2)+1):  # Percorrer cada linha entre y1 e y2
                x += tx
                print(y-Ymin)
                if bordas_esquerda[y-Ymin] == float('inf'):
                    bordas_esquerda[y-Ymin] = int(x)
                    bordas_direita[y-Ymin] = int(x)
                else:
                    bordas_esquerda[y-Ymin] = min(bordas_esquerda[y-Ymin], int(x))
                    bordas_direita[y-Ymin] = max(bordas_direita[y-Ymin], int(x))
            print("saiu")
    
    print(bordas_esquerda)
    print(bordas_direita)

# Exemplo de uso com um polígono de 4 lados:
vertices = [(1, 5), (3, 2), (7, 6), (5, 8)]

vertice_raster(vertices)




'''






    # Ordenar os vértices em ordem crescente de y
    vertices_ordenados = sorted(vertices, key=lambda v: v[1])

    # Obter coordenadas y mínimo e máximo
    y_min = vertices_ordenados[0][1]
    y_max = vertices_ordenados[-1][1]

    # Inicializar lista para armazenar as coordenadas x para cada y
    bordas_esquerda = [float('inf')] * (y_max - y_min + 1)
    bordas_direita = [-float('inf')] * (y_max - y_min + 1)

    # Calcular as bordas esquerda e direita para cada linha
    for i in range(len(vertices_ordenados)):
        j = (i + 1) % len(vertices_ordenados)  # Índice do próximo vértice
        x1, y1 = vertices_ordenados[i]
        x2, y2 = vertices_ordenados[j]

        if y1 != y2:  # Verificar se não é uma linha horizontal
            # Calcular a inclinação da aresta
            m = (x2 - x1) / (y2 - y1)

            # Percorrer cada linha entre y1 e y2
            for y in range(y1, y2 + 1):
                x = int(x1 + m * (y - y1))
                bordas_esquerda[y - y_min] = min(bordas_esquerda[y - y_min], x)
                bordas_direita[y - y_min] = max(bordas_direita[y - y_min], x)

    # Pintar pixel a pixel
    for y in range(y_min, y_max + 1):
        for x in range(bordas_esquerda[y - y_min], bordas_direita[y - y_min] + 1):
            # Pintar o pixel (x, y)
            print(f"Pintando pixel ({x}, {y})")
'''