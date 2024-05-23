

class WINDOW: # Definições da janela
    WIDTH = 800
    HEIGHT = 600
    TITLE = "Desenho de objeto para revolucionar"
    BACKGROUND = (255, 255, 255)

# Definições do desenho
class DESENHO:
    TITLE = "Objeto no sistema 3D"
    VP_min = [0, 0]
    VP_max = [800, 600]

    POINT_COLOR = (0, 0, 0)
    POINT_RADIUS = 3
    LINE_COLOR = (150, 150, 150)

    FACES = 10 # número de faces para revolução
    PROFUNDIDADE = 0  #Profundidade do objeto apos a revolução
    PERS = True  #Projeção perspectiva?
    HIDE_FACES = False #Esconder faces?

# Definições do botão
class BUTTON:
    WIDTH = 100
    HEIGHT = 30
    MARGIN = 10
    COLLOR = (200, 200, 200)

class TEXT:
    COLLOR = (0, 0, 0)

class CAMERA:
    VRP = [0, 600, 1200]
    dp = 1000
    Y = [0, 1, 0]
    