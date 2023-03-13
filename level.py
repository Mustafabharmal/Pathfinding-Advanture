from tkinter import Toplevel
import pygame as pg
from settings import *
from tile import Tile
from player import Player
from debug import *
from support import *
from random import choice
from TH_terminal import *


class Level:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pg.sprite.Group()
        self.create_map()

    def create_map(self):
        layouts = {
            'boundary':import_csv_layout('thunt_floor_blocks.csv'),
            'object':import_csv_layout('thunt_Objects_trees_rocks.csv')

        }
        graphics ={
            'grass':import_folder('graphics/grass'),
            'objects':import_folder('graphics/objects')
        }
        lst = []
        for style,layout in layouts.items():
            for row_index , row in enumerate(layout):
                for col_index , col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        lst.append((x,y))

                        if style == 'boundary':
                            Tile((x,y),[self.obstacle_sprites],'invisible')
                        # grass
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'grass',random_grass_image)
                        # object
                        if style == 'object':
                            try:
                                surf = graphics['objects'][int(col)]
                            except:
                                print(int(col))
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)
                            if(int(col) == 14):
                                print(f'({x},{y}),')
                    



        k,l = 2000,1500
        for i in DIALOG_OBJECT.keys():
            if DIALOG_OBJECT[i] == str(start_node):
                k,l = i
                break
        if start_node == 6709:
            l-=2*64
        else:
            k+=64


        self.player = Player((k,l), [self.visible_sprites] , self.obstacle_sprites  )
                
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        # debug(self.player.status) 
        debug(self.player.score)
        
        
                    
                
class YSortCameraGroup(pg.sprite.Group):
    def __init__(self ):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pg.math.Vector2()
        self.floor_surf = pg.image.load('graphics/tilemap/th.png').convert()
        self.floor_rect= self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self,player):
        # getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)
        for sprite in sorted(self.sprites() , key = lambda sprite:sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
        
    