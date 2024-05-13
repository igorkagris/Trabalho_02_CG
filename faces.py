
def cross(A, B): #A x B = vector
    return [A[1]*B[2] - A[2]*B[1],
            A[2]*B[0] - A[0]*B[2],
            A[0]*B[1] - A[1]*B[0]]    

def visibility(vertices, faces, VRP):
    # Cálculo do vetor normal
    visible_points = []
    visible_faces = []
    for face in faces:
        p1, p2, p3, p4 = face
        x1, y1, z1, h = vertices[p1]
        x2, y2, z2, h = vertices[p2]
        x3, y3, z3, h = vertices[p3]

        # Vetores
        vB_A = [x1-x2, y1-y2, z1-z2]
        vB_C = [x3-x2, y3-y2, z3-z2]

        #normal = vB_C x vB_A
        normal = cross(vB_C, vB_A)
        
        # equação do plano depende da constante, usando um ponto qualquer do plano temos:
        d = -(normal[0]*x2 + normal[1]*y2 + normal[2]*z2)
        #Substituindo os valores do VRP na equação do plano
        D = normal[0]*VRP[0] + normal[1]*VRP[1] + normal[2]*VRP[2] + d

        # Se D > 0, o observador está na frente do plano
        if D > 0:
            visible_faces.append(face)
            for i in face:
                if i not in visible_points:
                    visible_points.append(i)

    return visible_points, visible_faces