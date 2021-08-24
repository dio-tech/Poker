import os
import pygame

# ------------------------------------------
os.system('git add .')
os.system('git commit -m "Initial Commit"')
os.system('git push')
# ------------------------------------------

def redraw_window(win):
    win.fill((255, 255, 255))
    win.blit(pygame.image.load(os.path.join('assets', '10_of_clubs.png')), (0, 0))

WIDTH, HEIGHT = 1250, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main(win, width):
    run = True

    while run:
        redraw_window(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()

main(WIN, WIDTH)
