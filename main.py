import pygame, sys
from settings import *
import pygame 
from level import Level
from PIL import Image, ImageTk
from tkinter import PhotoImage
from tkinter_menu import *
# from pytmx.util_pygame import load_pygame

from player import main_sound




class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode ( (WIDTH, HEIGTH) )
        pygame.display.set_caption("Treasure Hunt")     
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load('graphics/background/BackgroundMenu1.png')
        DEFAULT_IMAGE_SIZE = (1920, 1080)
        self.bg = pygame.transform.scale(self.bg, DEFAULT_IMAGE_SIZE)
        self.resume_img = pygame.image.load('graphics/start_menu/resume.png').convert_alpha()
        self.exit_img = pygame.image.load('graphics/start_menu/exit.png').convert_alpha()
        # self.resume_btn = Button(100,200,self.resume_img)
        # self.exit_btn = Button(450,200,self.exit_img)
        # global data_tmx
        # data_tmx = load_pygame("/home/darshan/college/tiled2_fin/tmx/th.tmx")
        
        self.level = Level()

    def draw(self,x,y,image,scale):
        action = False
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width *scale),int(height *scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft=(x,y)
        self.screen.blit(self.image , (self.rect.x , self.rect.y))
        self.clicked = False
        # get mouse pos
        pos = pygame.mouse.get_pos()
        # print(pos)
        # check mouse and clicked conditions

        if self.rect.collidepoint(pos):#colliding or not
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action
    def pause(self):
        paused = True
        while paused:
            self.menu_sound = pygame.mixer.Sound('audio/menu_sound.mpeg')
            main_sound.set_volume(0)
            self.menu_sound.set_volume(0.5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                elif event.type == pygame.K_q:
                    pygame.quit()
                    quit()
        
            self.screen.blit(self.bg, (0, 0))
            if self.draw(550,365,self.resume_img,0.8):
                print("resume")
                paused = False
                main_sound.set_volume(0.8)

            if self.draw(550,545,self.exit_img,0.8):
                print('exit')
                exit()
            # pygame.draw.rect(self.screen,'red',(150,500,100,50))
            # debug("paused")
            pygame.display.update()
            self.clock.tick(5)

    def run(self):
        while True:
            # print("helloooooooo")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame .quit()  
                    sys.exit()
                

            self.screen.fill('black')
            self.level.run()
            if(pygame.key.get_pressed()[pygame.K_p]):
                # print("thereee")
                self.pause()
            # debug("hello:)")
            pygame.display.update()
            self.clock.tick(FPS)
    
# class Button(self):
    
   

if __name__ == '__main__':
    # m = Menu()
    pygame.mixer.init()
    pygame.mixer.music.load('audio/menu_sound.mpeg')
    pygame.mixer.music.play(-1)
    # m.create_menu()
    pygame.mixer.music.stop()

    game = Game()
    game.run()
