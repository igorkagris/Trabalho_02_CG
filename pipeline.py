from math import sqrt
from numpy import matmul

def normalize(v): #Correto (conferido)
    module = sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    normalized = [v[0]/module, v[1]/module, v[2]/module]
    return normalized

def dot(A, B):  #A * B = float
    return A[0]*B[0] + A[1]*B[1] + A[2]*B[2]

def cross(A, B): #A x B = vector
    return [A[1]*B[2] - A[2]*B[1],
            A[2]*B[0] - A[0]*B[2],
            A[0]*B[1] - A[1]*B[0]]    


def camera_transf_mat(vrp, p, Y): #Transformaçao SRU -> SRC
    translation_matrix = [[1, 0, 0, -vrp[0]],
                          [0, 1, 0, -vrp[1]],
                          [0, 0, 1, -vrp[2]],
                          [0, 0, 0,     1  ]]

    # Transformação de camera
    N = [(vrp[0] - p[0]), (vrp[1] - p[1]), (vrp[2] - p[2])] # N = VRP-P
    N = normalize(N)

    Y_x_n = dot(Y, N)
    V = [(Y[0] - (Y_x_n * N[0])),  # V = Y - (Y * N) * N #escrever toda a equação como generica para ser possivel mudar vetor Y
         (Y[1] - (Y_x_n * N[1])),
         (Y[2] - (Y_x_n * N[2]))]
    V = normalize(V)

    U = cross(V, N) # U = V x N (Como V e N são normalizados, U também é normalizado)


    # Matriz de transformação de camera
    transf_matrix= [[U[0], U[1], U[2],  0],
                    [V[0], V[1], V[2],  0],
                    [N[0], N[1], N[2],  0],
                    [  0 ,   0 ,   0 ,  1] ]
    return matmul(transf_matrix, translation_matrix)

def camera_viewport_mat(Xmin, Ymin, Xmax, Ymax, umin, vmin, umax, vmax): #Transformaçao SRC -> SRT
    du = umax - umin
    dv = vmax - vmin
    dx = Xmax - Xmin
    dy = Ymax - Ymin
    return [[ du/dx,   0  ,   0  ,-Xmin*(du/dx)+umin],
            [   0  ,-dv/dy,   0  , Ymin*(dv/dy)+vmax],
            [   0  ,   0  ,   1  ,       0          ],
            [   0  ,   0  ,   0  ,       1          ] ]
    

# Define a matriz de projeção
def pipeline(projpers, verts, vrp, p, dp, Y, Xmin, Ymin, Xmax, Ymax, umin, vmin, umax, vmax):
    
    camera_transf = camera_transf_mat(vrp, p, Y)

    if projpers: # Se for projeçao perspectiva
        camera_pers =  [[1,    0,    0,    0],
                        [0,    1,    0,    0],
                        [0,    0,    1,    0],
                        [0,    0,-1/dp,    0]]
        camera_transf = matmul(camera_pers, camera_transf)
    
    viewport_matrix = camera_viewport_mat(Xmin, Ymin, Xmax, Ymax, umin, vmin, umax, vmax)

    viewp_mat = matmul(viewport_matrix, camera_transf)

    # P' = viewp_mat * P
    viewp_points = []
    for vert in verts:
        x = viewp_mat[0][0]*vert[0] + viewp_mat[0][1]*vert[1] + viewp_mat[0][2]*vert[2] + viewp_mat[0][3]*1
        y = viewp_mat[1][0]*vert[0] + viewp_mat[1][1]*vert[1] + viewp_mat[1][2]*vert[2] + viewp_mat[1][3]*1
        z = viewp_mat[2][0]*vert[0] + viewp_mat[2][1]*vert[1] + viewp_mat[2][2]*vert[2] + viewp_mat[2][3]*1
        h = viewp_mat[3][0]*vert[0] + viewp_mat[3][1]*vert[1] + viewp_mat[3][2]*vert[2] + viewp_mat[3][3]*1
        viewp_points.append([x, y, z, h])

    return viewp_points