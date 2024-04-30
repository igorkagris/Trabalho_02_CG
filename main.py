import pygame
import sys
from config import *
from revolucao import revolucao
from pipeline import pipeline

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

# Centro do objeto
x_max = max([x for x, y in points])
x_min = min([x for x, y in points])
obj_center = [(x_min + x_max)/2, 0, DESENHO.PROFUNDIDADE]

# Faz a revolução dos pontos
vertices, edges = revolucao(points, DESENHO.FACES, DESENHO.PROFUNDIDADE)

'''#Exemplo do caderno para entrada
vertices.clear()
vertices.append([21.2, 0.7, 42.3])
vertices.append([34.1, 3.4, 27.2])
vertices.append([18.8, 5.6, 14.6])
vertices.append([5.9, 2.9, 29.7])
vertices.append([20, 20.9, 36.6])
obj_center = [20, 10, 25]'''

camera = [25, 15, 80] # Posição da câmera
dp = 40 # Distância do plano de projeção
vert_in_screen_pos = pipeline(vertices, camera, obj_center, dp)

for p in vert_in_screen_pos:
    print(p)





    #Faz uma tradução da tela para que o VRP fique no centro da tela
    for vert in vert_in_screen_pos:
        vert[0] += camera[0]
        vert[1] += camera[1]




running = True
while running:

    for event in pygame.event.get(): # Verifica eventos
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: # Coordenadas do clique
            points.append(event.pos)
        

    screen.fill(WINDOW.BACKGROUND) # Limpa a tela

    button_down = Create_button(screen, "-", ((WINDOW.WIDTH-1.5*BUTTON.WIDTH)/2)-0.4*BUTTON.WIDTH, BUTTON.MARGIN, 0.3)
    text = "Faces: " + str(DESENHO.FACES)
    text_faces = Create_button(screen, text, (WINDOW.WIDTH-1.5*BUTTON.WIDTH)/2 ,BUTTON.MARGIN , 1.5)
    button_up = Create_button(screen, "+", (WINDOW.WIDTH/2)+0.85*BUTTON.WIDTH, BUTTON.MARGIN, 0.3)
    button_clear = Create_button(screen, "Limpar", WINDOW.WIDTH - BUTTON.WIDTH - BUTTON.MARGIN, BUTTON.MARGIN, 1)

    mouse_pos = (0, 0) #define
    if len(points) != 0:    #mouse_pos = ultimo clique
        mouse_pos = points[-1]
    if button_down.collidepoint(*mouse_pos): # Verifica botão "-"
        points.pop()
        if (DESENHO.FACES > 20):
            DESENHO.FACES -= 10
        elif (DESENHO.FACES > 3):
            DESENHO.FACES -= 1
    elif button_up.collidepoint(*mouse_pos): # Verifica botão "+"
        points.pop()
        if (DESENHO.FACES < 20):
            DESENHO.FACES += 1
        elif (DESENHO.FACES < 1000):
            DESENHO.FACES += 10




    # Desenha os pontos
    for vert in vert_in_screen_pos:
        pygame.draw.circle(screen, DESENHO.POINT_COLOR, (int(vert[0]), int(vert[1])), DESENHO.POINT_RADIUS)

    pygame.display.flip() # Atualiza a tela