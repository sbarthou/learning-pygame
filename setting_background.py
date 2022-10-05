import pygame
from sys import exit


pygame.init()

# Screen
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Background')

# Background image
bg = pygame.image.load('assets/background/Blue Nebula/Blue_Nebula_02-1024x1024.png')
bg = pygame.transform.scale(bg, (size))   # scale image


running = True
# Main Loop
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(bg, (0, 0))
            
    pygame.display.update()
    
pygame.quit()
exit()