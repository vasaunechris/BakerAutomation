import pygame

class Windows:

    def __init__(self, gp):

        self.gamePainter = gp
        (width, height) = (300,300)#(self.gamePainter.getWidth(), self.gamePainter.getHeight())
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Test')
        background_colour = (255,255,255)
        self.screen.fill(background_colour)
        pygame.display.flip()

    @classmethod
    def paint(self):
        self.gamePainter.drawGame()
        pass


    

