

def intersection_calc(P_out, P_in, Xmin, Ymin, Xmax, Ymax):
    if P_out[0] <= Xmax and P_out[0] >= Xmin:
        if P_out[1] < Ymin: #Quando o ponto está acima da janela


        elif P_out[1] > Ymax: #Ponto está abaixo da janela 

    elif P_out[0] < Xmin: #P na esquerda
        #Realiza o recorte
    
    elif P_out[0] > Xmax: #P na direita



def recorte(A, Xmin, Ymin, Xmax, Ymax):
    L1 = [] #Polígono
    L2 = [] #Janela
    L3 = [] #Pontos entrando na janela
            #flag = 0 para dentro da viewport, 1 para fora
    for i in range (len(A)):

        if p[0] < Xmin  or p[0] > Xmax or p[1] < Ymin or p[1] > Ymax:
            if flag == 0: #Quando sai da viewport
                pn = intersection_calc(A, B, Xmin, Ymin, Xmax, Ymax)
                #L1.append(p interseção)
                #L2.append(p interseção)
            flag = 1
            #L1.append(pB)
        else:
            if flag == 1: #quando entra na viewport
                #Calcula interseção
                #L1.append(p interseção)
                #L2.append(p interseção)
                #L3.append(p interseção)
            flag = 0
        L1.append(A[i])
                
        flag = 0