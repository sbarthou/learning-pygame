import pygame

pygame.init()
font = pygame.font.Font(None, 30)

def debug(text, y = 10, x = 10):
    display_surf = pygame.display.get_surface()
    # Create some text
    debug_surf = font.render(str(text), True, 'white')
    # Create a rect with a pos
    debug_rect = debug_surf.get_rect(topleft = (x, y))
    pygame.draw.rect(display_surf, 'black', debug_rect)
    # Blit all
    display_surf.blit(debug_surf, debug_rect)