import pygame
from sys import exit


pygame.init()

# Screen
size = width, height = 700, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Eagle')
clock = pygame.time.Clock()


sprite_sheet_image = pygame.image.load('assets/eagle.png').convert_alpha()

def get_image(sheet, frame, width, height, scale):
    image = pygame.Surface((width, height)).convert_alpha()   # Creamos una superficie
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))   # Cargamos el area del sprite sheet en la superficie
    image = pygame.transform.scale(image, (width * scale, height * scale))
    return image


# Eagle Frame
frame_0 = get_image(sprite_sheet_image, 0, 32, 32, 2)


running = True


# Main Loop
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Background        
    screen.fill('#ffffff')
    
    # Show frame image
    screen.blit(frame_0, (0, 0))
            
    pygame.display.update()