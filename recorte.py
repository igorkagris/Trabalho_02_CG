


def recorte(A, Xmin, Ymin, Xmax, Ymax):
    #L1 = Polígono
    #L2 = Janela
    #L3 = Pontos entrando na janela
    #flag = 0 para dentro da viewport, 1 para fora
    for p in A:
        if p[0] < Xmin  or p[0] > Xmax or p[1] < Ymin or p[1] > Ymax:
            if flag == 0: #Quando sai da viewport
                pn = intersection_calc()
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
                
        flag = 0