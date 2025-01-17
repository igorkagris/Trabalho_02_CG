import math

def faces_points(in_3d, slices):
    faces = [] # Lista de faces anti-horária
    for i in range(slices):
        itens_linha = int((len(in_3d))/slices)
        for j in range(itens_linha):
            if i < slices-1:
                abaixo = i+1
            else:
                abaixo = 0
            if j < itens_linha-1:
                direita = j+1
            else:
                direita = 0
            faces.append([i*itens_linha+j, i*itens_linha+direita, abaixo*itens_linha+direita, abaixo*itens_linha+j])
    return faces


def counterclockwise_points(points):
    ymin = [-1, -1]
    for i in range(len(points)):
        if ymin[1] < points[i][1] or ymin[1] == -1:
            ymin = points[i]
            j = i
    
    if j!=0 and j!=len(points)-1:
                ant = points[j-1]
                prox = points[j+1]
    elif j == 0:
                ant = points[-1]
                prox = points[j+1]
    else:
                ant = points[j-1]
                prox = points[0]
        
    if ant[0] > prox[0]: #inverte a ordem dos pontos inseridos para ficar anti-horários
        return False
    else:
        return True


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

    if not counterclockwise_points(points):
        points[::-1]
        print("Pontos invertidos: ", points)
        
    for i in range (slices):
        [in_3D.append([x, y, 0]) for x, y in points]
        in_3D = rotacao_x(in_3D, rotation_slice)
    
    if profundidade != 0:
        in_3D = [[x, y, z+profundidade] for x, y, z in in_3D]

    faces = faces_points(in_3D, slices)

    obj_center = get_obj_center(in_3D)
    
    return in_3D, faces, obj_center

