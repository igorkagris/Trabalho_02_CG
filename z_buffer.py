#Válido apenas para polígonos convexos

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

rasterizar_vertices(vertices)