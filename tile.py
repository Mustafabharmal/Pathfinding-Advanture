import pygame as pg
from settings import *

class Tile(pg.sprite.Sprite):
    def __init__(self, pos,groups,sprite_type, surface = pg.Surface((TILESIZE,TILESIZE))) :
        super().__init__(groups)
        self.pos = pos
        self.sprite_type  = sprite_type
        # self.image = pg.image.load('graphics/test/rock.png').convert_alpha()
        self.image = surface
        self.id = id
        if sprite_type == 'object':
            # do an offset
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)