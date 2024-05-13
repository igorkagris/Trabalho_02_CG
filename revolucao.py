import math

def get_obj_center(vertices): #Calcula o centro do objeto
    x, y, z = 0, 0, 0

    for vert in vertices:
        x += vert[0]
        y += vert[1]
        z += vert[2]
    
    x /= len(vertices)
    y /= len(vertices)
    z /= len(vertices)
    return [x, y, z]

def rotacao_x(mat_a, graus): #Rotaciona em torno do eixo X
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
    
    if profundidade != 0:
        in_3D = [[x, y, z+profundidade] for x, y, z in in_3D]

    
    faces = [] # Lista de faces anti-horária (atual, abaixo, baixo_direita, direita)
    for i in range(slices):
        itens_linha = int((len(in_3D))/slices)
        for j in range(itens_linha):
            if i < slices-1:
                abaixo = i+1
            else:
                abaixo = 0
            if j < itens_linha-1:
                direita = j+1
            else:
                direita = 0
            faces.append([i*itens_linha+j, abaixo*itens_linha+j, abaixo*itens_linha+direita, i*itens_linha+direita])

    obj_center = get_obj_center(in_3D)
    return in_3D, faces, obj_center
