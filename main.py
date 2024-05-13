import pygame
import sys
from config import *
from revolucao import revolucao
from pipeline import pipeline
from faces import visibility
#from recorte import recorte

points = [] # Armazena os pontos clicados

def Create_button(surface, text, left, top, size): #Desenha botão predefinido
    button_rect = pygame.Rect(left, top, round(BUTTON.WIDTH*size), BUTTON.HEIGHT)
    pygame.draw.rect(surface, BUTTON.COLLOR, button_rect)  #retangulo
    text_surface = font.render(text, True, TEXT.COLLOR) #Texto
    text_rect = text_surface.get_rect(center=button_rect.center)
    surface.blit(text_surface, text_rect)
    return button_rect





# Inicializa a janela
pygame.init()
screen = pygame.display.set_mode((WINDOW.WIDTH, WINDOW.HEIGHT))
pygame.display.set_caption(WINDOW.TITLE)

try:
    pygame.display.get_init()
except: #Exception as error:
    print("Erro ao inicializar tela. ")#, error)

running = True                                                              # Janela para criar os pontos
while running:

    for event in pygame.event.get(): # Verifica eventos
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN: # Coordenadas do clique
            points.append(event.pos)

        elif event.type == pygame.KEYUP:
            
            if event.key == pygame.K_BACKSPACE:# Limpa tela quando '<-' é pressionado
                points.clear()
   
    screen.fill(WINDOW.BACKGROUND) # Limpa a tela
    
    font = pygame.font.Font(None, 26)
    # Desenha os Botões
    button_del_last = Create_button(screen, "Apagar", BUTTON.MARGIN, BUTTON.MARGIN, 1)
    button_ok = Create_button(screen, "Prosseguir", (WINDOW.WIDTH-BUTTON.WIDTH)/2, BUTTON.MARGIN, 1)
    button_clear = Create_button(screen, "Limpar", WINDOW.WIDTH - BUTTON.WIDTH - BUTTON.MARGIN, BUTTON.MARGIN, 1)

    #Verifica Cliques nos botões
    mouse_pos = (0, 0) #define
    if len(points) != 0:    #mouse_pos = ultimo clique
        mouse_pos = points[-1]

    if button_del_last.collidepoint(*mouse_pos): # Verifica botão "Apagar"
        points.pop()
        if len(points) != 0:
            points.pop()
    elif button_ok.collidepoint(*mouse_pos): # Verifica botão "Prosseguir"
        points.pop()
        if len(points) > 2:
            break
    elif button_clear.collidepoint(*mouse_pos): # Verifica botão "Limpar"
        points.clear()
        
    # Redesenha os pontos
    for point in points:
        pygame.draw.circle(screen, DESENHO.POINT_COLOR, point, DESENHO.POINT_RADIUS)

    if len(points) > 2: # Desenha linhas entre os pontos (a partir do terceiro ponto)
        for i in range(len(points) - 1):
            pygame.draw.line(screen, DESENHO.LINE_COLOR, points[i], points[i + 1])
        half_collor = ((DESENHO.LINE_COLOR[0]/2), (DESENHO.LINE_COLOR[1]/2), (DESENHO.LINE_COLOR[2]/2))
        pygame.draw.line(screen, half_collor, points[-1], points[0])

    pygame.display.flip() # Atualiza a tela

#inverte o desenho em y
points = [[x, WINDOW.HEIGHT-y] for x, y in points]

# Faz a revolução dos pontos
vertices, faces, obj_center = revolucao(points, DESENHO.FACES, DESENHO.PROFUNDIDADE)


'''#Exemplo das planilhas para entrada
vertices.clear()
vertices.append([21.2, 0.7, 42.3])
vertices.append([34.1, 3.4, 27.2])
vertices.append([18.8, 5.6, 14.6])
vertices.append([5.9, 2.9, 29.7])
vertices.append([20, 20.9, 31.6])
obj_center = [20, 10, 25]
vert_in_screen_pos = pipeline(False, vertices, CAMERA.VRP, obj_center, CAMERA.dp, CAMERA.Y, -20, -15, 20, 15, 0, 0, 319, 239)

for vert in vert_in_screen_pos:
    print(vert)'''

#Vertices na posição de tela vert_.[n] = [x, y, z, h]
                               # pontos,  camera, centro objeto,     dp ,  vetor Y,  Coordenadas de tela, e de viewport
vert_in_screen_pos = pipeline(DESENHO.PERS, vertices, CAMERA.VRP, obj_center, CAMERA.dp, CAMERA.Y, 0, -WINDOW.HEIGHT, WINDOW.WIDTH, WINDOW.HEIGHT, DESENHO.VP_min[0], DESENHO.VP_min[1], DESENHO.VP_max[0], DESENHO.VP_max[1])
                                                                                                    #(-WINDOW.HEIGHT) Duplica altura em Y para centralizar o objeto desenhado
visible_points, visible_faces = visibility(vert_in_screen_pos, faces, CAMERA.VRP)



#Centraliza os pontos na tela através de gambiarra
for i in range(len(vert_in_screen_pos)):
    vert_in_screen_pos[i][0] += DESENHO.VP_max[0]/2


# Reconfigura a janela
screen = pygame.display.set_mode((DESENHO.VP_max[0], DESENHO.VP_max[1]))
pygame.display.set_caption(DESENHO.TITLE)
running = True
while running:

    for event in pygame.event.get(): # Verifica eventos
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: # Coordenadas do clique
            points.append(event.pos)

    screen.fill(WINDOW.BACKGROUND) # Limpa a tela

    button_down = Create_button(screen, "-", ((DESENHO.VP_max[0]-1.5*BUTTON.WIDTH)/2)-0.4*BUTTON.WIDTH, BUTTON.MARGIN, 0.3)
    text = "Faces: " + str(DESENHO.FACES)
    text_faces = Create_button(screen, text, (DESENHO.VP_max[0]-1.5*BUTTON.WIDTH)/2 ,BUTTON.MARGIN , 1.5)
    button_up = Create_button(screen, "+", (DESENHO.VP_max[0]/2)+0.85*BUTTON.WIDTH, BUTTON.MARGIN, 0.3)
    button_clear = Create_button(screen, "Ocultar Faces", DESENHO.VP_max[0] - BUTTON.WIDTH - BUTTON.MARGIN, BUTTON.MARGIN, 1)

    #Verifica Cliques nos botões
    mouse_pos = (0, 0) #define
    if len(points) != 0:    #mouse_pos = ultimo clique
        mouse_pos = points[-1]
    if button_down.collidepoint(*mouse_pos): # Verifica botão "-"
        points.pop()
        if DESENHO.FACES > 20:
            DESENHO.FACES -= 10
        elif DESENHO.FACES > 3:
            DESENHO.FACES -= 1
    if button_up.collidepoint(*mouse_pos): # Verifica botão "+"
        points.pop()
        if DESENHO.FACES < 20:
            DESENHO.FACES += 1
        elif DESENHO.FACES >= 20:
            DESENHO.FACES += 10
    if button_clear.collidepoint(*mouse_pos): # Verifica botão "Ocultar Faces"
        points.pop()
        DESENHO.HIDE_FACES = not DESENHO.HIDE_FACES

    #Transforma todas as arestas em inteiros em coordenadas de tela.
    wdw = [] 
    for vert in vert_in_screen_pos:
        wdw.append([int(vert[0]/vert[3]), int(vert[1]/vert[3])])
        

    #Realiza o recorte das arestas que estão fora da viewport
    #wdw = recorte(wdw, DESENHO.VP_min[0], DESENHO.VP_min[1], DESENHO.VP_max[0], DESENHO.VP_max[1])

    # Desenha os pontos
    for i in range (len(wdw)):
        if i in visible_points or DESENHO.HIDE_FACES == False:
            pygame.draw.circle(screen, DESENHO.POINT_COLOR, (int(wdw[faces[i][0]][0]), int(wdw[faces[i][0]][1])), DESENHO.POINT_RADIUS)

        # Desenha as arestas entre o vertive atual e o da direita e de baixo
        drawed_edges = []
        if (faces[i] in visible_faces) or (DESENHO.HIDE_FACES == False):    #Fazer toda a esquematização para não desenhar arestas repetidas OU REDESENHA-LAS?
            edge_to_draw = [min(i, faces[i][1]), max(i, faces[i][1])]

            if edge_to_draw not in drawed_edges: #Desenha arestas entre o vertice atual (i == faces[i][0]) e o vértice de baixo (faces[i][1]) --
                pygame.draw.line(screen, DESENHO.LINE_COLOR, (wdw[faces[i][0]][0], wdw[faces[i][0]][1]), (wdw[faces[i][1]][0], wdw[faces[i][1]][1]))
                drawed_edges.append(edge_to_draw)
            edge_to_draw = [min(i, faces[i][3]), max(i, faces[i][3])]
            if edge_to_draw not in drawed_edges: #Desenha arestas entre o vertice atual (i == faces[i][0]) e o vértice da direita (faces[i][3]) |
                pygame.draw.line(screen, DESENHO.LINE_COLOR, (wdw[faces[i][0]][0], wdw[faces[i][0]][1]), (wdw[faces[i][3]][0], wdw[faces[i][3]][1]))
                drawed_edges.append(edge_to_draw)
            edge_to_draw = [min(faces[i][1], faces[i][2]), max(faces[i][1], faces[i][2])]
            if edge_to_draw not in drawed_edges: #Desenha arestas entre o vertice de baixo (faces[i][1]) e o vértice baixo-direita (faces[i][2]) --
                pygame.draw.line(screen, DESENHO.LINE_COLOR, (wdw[faces[i][1]][0], wdw[faces[i][1]][1]), (wdw[faces[i][2]][0], wdw[faces[i][2]][1]))
                drawed_edges.append(edge_to_draw)
            edge_to_draw = [min(faces[i][2], faces[i][3]), max(faces[i][2], faces[i][3])]
            if edge_to_draw not in drawed_edges: #Desenha arestas entre o vertice baixo-direita (faces[i][2]) e o vértice da direita (faces[i][3]) |
                pygame.draw.line(screen, DESENHO.LINE_COLOR, (wdw[faces[i][2]][0], wdw[faces[i][2]][1]), (wdw[faces[i][3]][0], wdw[faces[i][3]][1]))
                drawed_edges.append(edge_to_draw)

    pygame.display.flip() # Atualiza a tela
