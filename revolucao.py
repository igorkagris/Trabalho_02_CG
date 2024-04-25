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


def revolucao(points, slices):
    in_3D = []

    rotation_slice = 360/slices

    for i in range (slices):
        [in_3D.append([x, y, 0]) for x, y in points]
        in_3D = rotacao_x(in_3D, rotation_slice)

    return in_3D
            
        

