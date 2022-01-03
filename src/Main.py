from engine.Windows import *
from engine.GamePainter import *

def main():
    gp = GamePainter()
    win = Windows(gp)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()