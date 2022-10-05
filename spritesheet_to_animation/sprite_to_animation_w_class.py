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

# Create animation list
animation_list = []
animation_steps = 3
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0

for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(x, 32, 32, 2))


running = True


# Main Loop
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Background        
    screen.fill('#ffffff')
    
    # Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0
    
    # Show frame image
    screen.blit(animation_list[frame], (0, 0))
            
    pygame.display.update()