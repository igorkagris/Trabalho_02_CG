

def tbrl_flag(P, Xmin, Ymin, Xmax, Ymax):
    t, b, r, l = 0, 0, 0, 0 #top, bottom, right, left

    if P[1] < Ymin: #P acima
        t = 1
    if P[1] > Ymax: #P abaixo
        b = 1
    if P[0] >= Xmax: #P na direita
        r = 1
    if P[0] <= Xmin: #P na esquerda
        l = 1
    return [t, b, r, l]

def top_cut(A, tbrl, Ymin):
    B = []
    for i in range(len(A)): 
        if i == len(A)-1: #proximo ponto: i -> j = aresta
            j=0
        else: 
            j=i+1
        
        if tbrl[i][0] == 0 and tbrl[j][0] ==  0: #ambos dentro 
            B.append(A[j]) #salva prox
        elif (tbrl[i][0] == 1 and tbrl[j][0] == 0): #adentrando a area de recorte 
            x = A[i][0] + (Ymin - A[i][1]) * ((A[j][0] - A[i][0])/(A[j][1] - A[i][1])) #salva recorte e prox

            B.append([x, Ymin])
            B.append(A[j])
        
        elif tbrl[i][0] == 0 and tbrl[j][0] == 1: #saindo da area de recorte
            x = A[i][0] + (Ymin - A[i][1]) * ((A[j][0] - A[i][0])/(A[j][1] - A[i][1])) #salva recorte

            B.append([x, Ymin])
        else: #ambos fora
            pass
        
    return B
    
def bottom_cut(A, tbrl, Ymax):
    B = []
    for i in range(len(A)): 
        if i == len(A)-1: #proximo ponto: i -> j = aresta
            j=0
        else: 
            j=i+1
        
        if tbrl[i][1] == 0 and tbrl[j][1] ==  0: #ambos dentro 
            B.append(A[j]) #salva prox
        elif (tbrl[i][1] == 1 and tbrl[j][1] == 0): #adentrando a area de recorte
            x = A[i][0] + (Ymax - A[i][1]) * ((A[j][0] - A[i][0])/(A[j][1] - A[i][1])) #salva recorte e prox

            B.append([x, Ymax])
            B.append(A[j])
        
        elif tbrl[i][1] == 0 and tbrl[j][1] == 1: #saindo da area de recorte
            x = A[i][0] + (Ymax - A[i][1]) * ((A[j][0] - A[i][0])/(A[j][1] - A[i][1])) #salva recorte

            B.append([x, Ymax])
        else: #ambos fora
            pass
        
    return B

def right_cut(A, tbrl, Xmax):
    B = []
    for i in range(len(A)): 
        if i == len(A)-1: #proximo ponto: i -> j = aresta
            j=0
        else: 
            j=i+1
        
        if tbrl[i][2] == 0 and tbrl[j][2] ==  0: #ambos dentro 
            B.append(A[j]) #salva prox
        elif (tbrl[i][2] == 1 and tbrl[j][2] == 0): #adentrando a area de recorte
            y = A[i][1] + (Xmax - A[i][0]) * ((A[j][1] - A[i][1])/(A[j][0] - A[i][0])) #salva recorte e prox

            B.append([Xmax, y])
            B.append(A[j])
        
        elif tbrl[i][2] == 0 and tbrl[j][2] == 1: #saindo da area de recorte
            y = A[i][1] + (Xmax - A[i][0]) * ((A[j][1] - A[i][1])/(A[j][0] - A[i][0])) #salva recorte

            B.append([Xmax, y])
        else: #ambos fora
            pass
        
    return B

def left_cut(A, tbrl, Xmin):
    B = []
    for i in range(len(A)): 
        if i == len(A)-1: #proximo ponto: i -> j = aresta
            j=0
        else: 
            j=i+1
        
        if tbrl[i][3] == 0 and tbrl[j][3] ==  0: #ambos dentro 
            B.append(A[j]) #salva prox
        elif (tbrl[i][3] == 1 and tbrl[j][3] == 0): #adentrando a area de recorte
            y = A[i][1] + (Xmin - A[i][0]) * ((A[j][1] - A[i][1])/(A[j][0] - A[i][0])) #salva recorte e prox

            B.append([Xmin, y])
            B.append(A[j])
        
        elif tbrl[i][3] == 0 and tbrl[j][3] == 1: #saindo da area de recorte
            y = A[i][1] + (Xmin - A[i][0]) * ((A[j][1] - A[i][1])/(A[j][0] - A[i][0])) #salva recorte

            B.append([Xmin, y])
        else: #ambos fora
            pass
        
    return B 

def recorte(A, Xmin, Ymin, Xmax, Ymax):

    tbrl = []
    for a in A: tbrl.append(tbrl_flag(a, Xmin, Ymin, Xmax, Ymax)) #precisa recriar TBRL pois a lista é rearranjada
    A = top_cut(A, tbrl, Ymin)

    tbrl.clear()
    for a in A: tbrl.append(tbrl_flag(a, Xmin, Ymin, Xmax, Ymax))
    A = bottom_cut(A, tbrl, Ymax)

    tbrl.clear()
    for a in A: tbrl.append(tbrl_flag(a, Xmin, Ymin, Xmax, Ymax))
    A = right_cut(A, tbrl, Xmax)

    tbrl.clear()
    for a in A: tbrl.append(tbrl_flag(a, Xmin, Ymin, Xmax, Ymax))
    A = left_cut(A, tbrl, Xmin)

    return A

    
''' #Função de teste:
A = [(1,1),(1,5),(5,5),(5,1)]
Xmin, Ymin, Xmax, Ymax = 2, 2, 4, 4

print(recorte(A, Xmin, Ymin, Xmax, Ymax))
'''

    
