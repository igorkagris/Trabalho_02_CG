from math import sqrt
from numpy import matmul

def normalize(v):
    module = sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    normalized = [v[0]/module, v[1]/module, v[2]/module]
    return normalized


def camera_transf_mat(vrp, p):
    # Transformação de camera
    N_vector = [(vrp[0] - p[0]), (vrp[1] - p[1]), (vrp[2] - p[2])] # N = VRP-P
    N_vector = normalize(N_vector)

    V_vector = [-(N_vector[2] - N_vector[0]) * N_vector[0],  # V = Y - (Y * N) * N
                 1 - (N_vector[2] - N_vector[0]) * N_vector[1],
                 -(N_vector[2] - N_vector[0]) * N_vector[2]]
    print(V_vector)
    V_vector = normalize(V_vector)

    U_vector = [V_vector[1]*N_vector[2] - V_vector[2]*N_vector[1], # U = N x V
                V_vector[2]*N_vector[0] - V_vector[0]*N_vector[2],
                V_vector[0]*N_vector[1] - V_vector[1]*N_vector[0]]
    print(U_vector)
    U_vector = normalize(U_vector)

    print(U_vector)
    print(V_vector)
    print(N_vector)
    # Matriz de transformação de camera
    return     [[U_vector[0], U_vector[1], U_vector[2], -vrp[0]],
                [V_vector[0], V_vector[1], V_vector[2], -vrp[1]],
                [N_vector[0], N_vector[1], N_vector[2], -vrp[2]],
                [      0    ,       0    ,       0    ,     1  ]]


    # Define a matriz de projeção
def pipeline(width, height, verts, vrp, p, dp):
    
    camera_transf = camera_transf_mat(vrp, p)
    print("camera Trans:", camera_transf)

    camera_pers =  [[1,    0,    0,    0],
                    [0,    1,    0,    0],
                    [0,    0,    1,    0],
                    [0,    0, 1/dp,    0]]
    
    viewp_mat = matmul(camera_pers, camera_transf)

    print(viewp_mat)

    viewp_points = []
    for vert in verts:
        x = viewp_mat[0][0]*vert[0] + viewp_mat[0][1]*vert[1] + viewp_mat[0][2]*vert[2] + viewp_mat[0][3]*1
        y = viewp_mat[1][0]*vert[0] + viewp_mat[1][1]*vert[1] + viewp_mat[1][2]*vert[2] + viewp_mat[1][3]*1
        z = viewp_mat[2][0]*vert[0] + viewp_mat[2][1]*vert[1] + viewp_mat[2][2]*vert[2] + viewp_mat[2][3]*1
        h = viewp_mat[3][0]*vert[0] + viewp_mat[3][1]*vert[1] + viewp_mat[3][2]*vert[2] + viewp_mat[3][3]*1
        viewp_points.append([round(x/h, 6), round(y/h, 6), round(z, 6), round(h, 6)])

    return viewp_points