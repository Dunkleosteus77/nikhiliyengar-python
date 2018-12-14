import pygame, random

class Game:
    def __init__(self, width=1000, height=1000, fps=50, x=0, y=0):
        self.width = width
        self.height = height
        self.fps = fps
        self.running = False
        self.x=x
        self.y=y

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()

        position_x = random.randint(0, self.width)
        position_y = random.randint(0, self.height)
        v_x = 1 + (1/3)*self.clock
        v_y = 1 * (1/3)*self.clock

class Circle(Game):
    def __init__(self, width=1000, height=1000, fps=50, x=0, y=0):
        Game.__init__(self, width, height, fps, x, y)
    radius=20
    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go = False
        screen.fill((0,0,0))
        pygame.draw.circle(screen, (x,y), radius)
        pygame.display.update()
