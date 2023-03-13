from pytmx.util_pygame import load_pygame

import pygame, sys
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode ( (400, 600) )
        pygame.display.set_caption("Treasure Hunt") 
        self.clock = pygame.time.Clock()
        self.data_tmx = load_pygame("/home/darshan/college/tiled2_fin/tmx/th.tmx")
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame .quit()
                    sys.exit()
            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(60)
    def any(self):
        self.tmx_data = load_pygame('/home/darshan/college/tiled2_fin/tmx/th.tmx')
        tile_layer = self.tmx_data.get_layer_by_name('Objects_trees_rocks')
        print(self.tmx_data.objects_by_id)
if __name__ == '__main__':
    game = Game()
    game.any()
    game.run()
