

class WINDOW: # Definições da janela
    WIDTH = 1280
    HEIGHT = 720
    TITLE = "Desenho de pontos e linhas"
    BACKGROUND = (255, 255, 255)

class VIEWPORT: # Definições da viewport
    WIDTH = 800
    HEIGHT = 600


# Definições do desenho
class DESENHO:
    POINT_COLOR = (255, 0, 0)
    POINT_RADIUS = 5
    LINE_COLOR = (0, 0, 255)
    FACES = 4 # número de faces para revolução
    PROFUNDIDADE = 100  #Profundidade do objeto apos a revolução

# Definições do botão
class BUTTON:
    WIDTH = 100
    HEIGHT = 30
    MARGIN = 10
    COLLOR = (200, 200, 200)

class TEXT:
    COLLOR = (0, 0, 0)
