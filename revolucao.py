import math

def rotacao_x(mat_a, graus):
    rad = math.radians(graus)
    sen = math.sin(rad)
    cos = math.cos(rad)
    '''mat_rot = {(1,  0 ,   0 ),
               (0, cos, -sen),
               (0, sen,  cos)}'''

    for i in range(len(mat_a)):
        x, y, z = mat_a[i]
        #x = x
        y2 = round(y*cos + z*(-sen), 6)
        z = round(y*sen + z*cos, 6)

        mat_a[i] = [x, y2, z]
    
    return mat_a

def revolucao(points, slices, profundidade):
    in_3D = []
    rotation_slice = 360/slices
    
    for i in range (slices):
        [in_3D.append([x, y, 0]) for x, y in points]
        in_3D = rotacao_x(in_3D, rotation_slice)
    
    in_3D = [[x, y, z+profundidade] for x, y, z in in_3D]

    edges = [] # Lista de arestas (esquerda, direita, acima, abaixo)
    for i in range(slices):
        itens_linha = int((len(in_3D))/slices)
        for j in range(itens_linha):
            if i == 0:
                acima = slices-1
                abaixo = i+1
            elif i < slices-1:
                acima = i-1
                abaixo = i+1
            else:
                acima = i-1
                abaixo = 0
            if j == 0:
                esquerda = itens_linha-1
                direita = j+1
            elif j < itens_linha-1:
                esquerda = j-1
                direita = j+1
            else:
                esquerda = j-1
                direita = 0
            edges.append([i*itens_linha+esquerda, i*itens_linha+direita, acima*itens_linha+j, abaixo*itens_linha+j])

    faces = []
    
    return in_3D, edges
