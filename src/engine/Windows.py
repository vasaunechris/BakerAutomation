import pygame

class Window:

    def __init__(self, gp):

        self.gamePainter = gp
        background_colour = (255,255,255)
        (width, height) = (self.gamePainter.getWidth(), self.gamePainter.getHeight())
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Test')
        self.screen.fill(background_colour)
        pygame.display.flip()
        

    def paint(self):
        self.gamePainter.draw()


    

