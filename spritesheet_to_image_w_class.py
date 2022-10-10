import pygame
from sys import exit


pygame.init()

# Screen
size = width, height = 700, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Eagle')


class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
        
    def get_image(self, frame, width, height, scale):
        image = pygame.Surface((width, height)).convert_alpha()   # Creamos una superficie
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))   # Cargamos el area del sprite sheet en la superficie
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image


sprite_sheet_image = pygame.image.load('assets/eagle.png').convert_alpha()
sprite_sheet = SpriteSheet(sprite_sheet_image)


frame_0 = sprite_sheet.get_image(0, 32, 32, 2)
frame_1 = sprite_sheet.get_image(1, 32, 32, 2)


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
    screen.blit(frame_1, (100, 0))
            
    pygame.display.update()