import pygame

pygame.init()

font = pygame.font.Font('graphics/font/joystix.ttf', 30)

def debug(info,y = 10, x = 10):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(f'Score: {str(info)}', True, 'White' )
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    # pygame. draw.rect(display_surface, 'Black',debug_rect)
    display_surface.blit(debug_surf,debug_rect)

def show_jey(info,y = 10, x = 885):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'Yellow' )
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame. draw.rect(display_surface, 'Black',debug_rect)
    display_surface.blit(debug_surf,debug_rect)