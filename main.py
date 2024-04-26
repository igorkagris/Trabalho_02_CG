import pygame
import sys
from config import *
from revolucao import revolucao
from pipeline import pipeline

points = [] # Armazena os pontos clicados

def clear_points(): # Limpa os pontos
    points.clear()

def Create_button(surface, text, left, top): #Desenha botão predefinido
    button_rect = pygame.Rect(left, top, BUTTON.WIDTH, BUTTON.HEIGHT)
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

running = True
while running:

    for event in pygame.event.get(): # Verifica eventos
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN: # Coordenadas do clique
            points.append(event.pos)

        elif event.type == pygame.KEYUP:
            
            if event.key == pygame.K_BACKSPACE:# Limpa tela quando '<-' é pressionado
                clear_points()
   
    screen.fill(WINDOW.BACKGROUND) # Limpa a tela
    
    font = pygame.font.Font(None, 26)
    # Desenha os Botões
    button_del_last = Create_button(screen, "Apagar", BUTTON.MARGIN, BUTTON.MARGIN)
    button_ok = Create_button(screen, "Prosseguir", (WINDOW.WIDTH-BUTTON.WIDTH)/2, BUTTON.MARGIN)
    button_clear = Create_button(screen, "Limpar", WINDOW.WIDTH - BUTTON.WIDTH - BUTTON.MARGIN, BUTTON.MARGIN)

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
        break
    elif button_clear.collidepoint(*mouse_pos): # Verifica botão "Limpar"
        clear_points()
        
    # Redesenha os pontos
    for point in points:
        pygame.draw.circle(screen, DESENHO.POINT_COLOR, point, DESENHO.POINT_RADIUS)

    if len(points) >= 2: # Desenha linhas entre os pontos (a partir do segundo ponto)
        for i in range(len(points) - 1):
            pygame.draw.line(screen, DESENHO.LINE_COLOR, points[i], points[i + 1])

    pygame.display.flip() # Atualiza a tela

#inverte o denenho em y
points = [[x, WINDOW.HEIGHT-y] for x, y in points]

# Centro do objeto
x_max = max([x for x, y in points])
x_min = min([x for x, y in points])
obj_center = [(x_min + x_max)/2, 0, DESENHO.PROFUNDIDADE]

# Faz a revolução dos pontos
vertices = revolucao(points, DESENHO.FACES, DESENHO.PROFUNDIDADE)


camera = [0, 0, 0] # Posição da câmera
dp = 30 # Distância do plano de projeção
vert_screen_pos = pipeline(WINDOW.WIDTH, WINDOW.HEIGHT, vertices, camera, obj_center, dp)

pygame.init()
screen = pygame.display.set_mode((WINDOW.WIDTH, WINDOW.HEIGHT))
pygame.display.set_caption(WINDOW.TITLE)

screen.fill(WINDOW.BACKGROUND)
for vert in vert_screen_pos:
    if (vert[0] >= 0 and vert[0] < WINDOW.WIDTH and vert[1] >= 0 and vert[1] < WINDOW.HEIGHT):
        print("1")
        pygame.draw.circle(screen, DESENHO.POINT_COLOR, [round(vert[0]), round(vert[1])], DESENHO.POINT_RADIUS)


    '''if len(vert_screen_pos) >= 2: # Desenha linhas entre os pontos (a partir do segundo ponto)
        for i in range(len(vert_screen_pos) - 1):
            pygame.draw.line(screen, DESENHO.LINE_COLOR, vert_screen_pos[i], vert_screen_pos[i + 1])
'''
pygame.display.flip() # Atualiza a tela
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()