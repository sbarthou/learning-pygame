import pygame, sys
from debug import debug


pygame.init()

# Screen
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Background')


running = True
# Main Loop
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill('white')
    
    debug(pygame.mouse.get_pos())
    debug(pygame.mouse.get_pressed(), 40)
    debug('mouse', pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])
            
    pygame.display.update()