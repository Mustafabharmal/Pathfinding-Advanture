from math import sin
import time
from image_show import *
# from test import *
from easygui import *
import pygame as pg
from settings import *
from easygui_get_input import *
from support import import_folder
from random import choice
from debug import *
from TH_terminal import *
main_sound = pygame.mixer.Sound('audio/main.ogg')

class Player(pg.sprite.Sprite ):
    def __init__(self, pos,groups,obstacle_sprites) :
        super().__init__(groups)
        self.image = pg.image.load('graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.wrong_ans = 0
        self.keyy = 0



        self.direction = pg.math.Vector2()#gives x and y default 0 and 0
        self.speed = 5;
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.obstacle_sprites =  obstacle_sprites

        main_sound.play(loops=-1)
        self.game_over = pygame.mixer.Sound('audio/game_over.mpeg')
        self.game_over.set_volume(0.9)
        self.death_sound = pg.mixer.Sound('audio/death.wav')
        self.mario_win = pg.mixer.Sound('audio/mario_win.mpeg')
        self.death_sound.set_volume(0.8)
        self.mario_win.set_volume(0.9)

        self.score = 0
        self.max_score = len(node_traversal_longest_shortest_path)*100

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0 
    
        
    def import_player_assets(self):
        character_path = 'graphics/player/'
        self.animations = {'up' : ['graphics/player/up'],'down' : [] , 'left' :[] , 'right' : [],
                            'up_idle' : [],'down_idle' : [] , 'left_idle' :[] , 'right_idle' : [],
                            'up_attack' : [],'down_attack' : [] , 'left_attack' :[] , 'right_attack' : []}
        for animation in self.animations.keys():
            full_path = character_path +animation
            self.animations[animation] = import_folder(full_path)
    
    def input(self):# getting keyboard input to move the player

        if not self.attacking:
            keys =  pg.key.get_pressed()
            
            if(keys[pg.K_LALT] and keys[pg.K_k]):
                show_jey(self.keyy)

            if(keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT]):
                self.speed = 10;
                if keys[pg.K_UP] or keys[pg.K_w]:
                    self.direction.y = -1
                    self.status = 'up'
                elif keys[pg.K_DOWN] or keys[pg.K_s] :
                    self.direction.y = 1
                    self.status = 'down'
                else :
                    self.direction.y = 0
                if keys[pg.K_RIGHT] or keys[pg.K_d]:
                    self.direction.x = 1
                    self.status = 'right'
                elif keys[pg.K_LEFT] or keys[pg.K_a]:
                    self.direction.x = -1
                    self.status = 'left'
                    
                else :
                    self.direction.x = 0
            else:
                self.speed = 5
                if keys[pg.K_UP] or keys[pg.K_w]:
                    self.direction.y = -1
                    self.status = 'up'
                elif keys[pg.K_DOWN] or keys[pg.K_s]:
                    self.direction.y = 1
                    self.status = 'down'
                else :
                    self.direction.y = 0

                if keys[pg.K_RIGHT] or keys[pg.K_d]:
                    self.direction.x = 1
                    self.status = 'right'
                elif keys[pg.K_LEFT] or keys[pg.K_a]:
                    self.direction.x = -1
                    self.status = 'left'
                else :
                    self.direction.x = 0


            if keys[pg.K_SPACE]  and not self.attacking:
                self.attacking = True
                self.attack_time = pg.time.get_ticks()

                print('attack')

            if keys[pg.K_LCTRL]  and not self.attacking:
                self.attacking = True
                self.attack_time = pg.time.get_ticks()

                print('magic')
    def get_status(self):
        if self.direction.x == 0 and  self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status :
                self.status += "_idle"

        if self.attacking:
            self.direction.x =0
            self.direction.y = 0
            if 'idle' in self.status:
                self.status = self.status.replace('_idle','_attack')
            if not 'attack' in self.status:
                self.status += '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','')
    def move(self,speed):
        if self.direction.magnitude() != 0: #vector of  0 cant be normalized hence if statement pygame gives error
            self.direction = self.direction.normalize()# correcting the speed ,as speed increases diagonally pressing down and right at the same time for eg..
        
        self.hitbox.x += self.direction.x * speed
        self.collision ('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision ('vertical')
        
        self.rect.center = self.hitbox.center
    def collision(self,direction):
        
        if direction == 'horizontal':
            
            for sprite in self.obstacle_sprites:
                
                if sprite.hitbox.colliderect(self.hitbox):#tells if collision happened or not
                    if self.direction.x > 0:#moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:#moving left
                        self.hitbox.left = sprite.hitbox.right
                    

                    if(sprite.pos in DIALOG_OBJECT.keys()):
                        self.death_sound.play()
                        if DIALOG_OBJECT[sprite.pos] == str(start_node) :
                            key = DIALOG_OBJECT[sprite.pos]

                        else:
                            key = get_input("Please enter the key :")

                        if key == DIALOG_OBJECT[sprite.pos]:

                            que = choice(list(QUESTIONS.keys()))
                            
                            print(que)
                            ans=""
                            ans = enterbox(que)
                            print(type(ans))
                            if(ans==None):
                                print('ffffffffffffffffffff')
                                ans=""

                            if ans.lower() == QUESTIONS[que].lower():
                                if(str(key) == node_traversal_longest_shortest_path[-1]):
                                    if self.score == self.max_score :
                                        show(f'Congratulations!! you won with maximum score possible')
                                    else :
                                        show(f'You won. you could have scored {self.max_score - self.score} more.')
                                    main_sound.fadeout(3)

                                    self.mario_win.play()
                                    time.sleep(8)

                                    exit()
                                else:
                                    show(f'Your ans is correct \n{node_traversal_longest_shortest_path[node_traversal_longest_shortest_path.index(int(key))+1]} is your next target ')
                                    self.score += 100
                                    self.keyy = {node_traversal_longest_shortest_path[node_traversal_longest_shortest_path.index(int(key))+1]}
                            else:
                                self.wrong_ans+=1
                                self.score -= 50

                                if self.wrong_ans >=5 :
                                    alpha = self.wave_value()
                                    self.image.set_alpha(alpha)
                                    show('GAME OVER')
                                    main_sound.fadeout(2)

                                    self.game_over.play()
                                    
                                    
                                    time.sleep(6)

                                    exit()
                                show('Your ans is incorrect')
                        else:
                            show('Enter a valid key.')
                        
            
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):#telss if collision happened or not
                    if self.direction.y > 0:#moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:#moving up
                        self.hitbox.top = sprite.hitbox.bottom

                    if(sprite.pos in DIALOG_OBJECT.keys()):
                        self.death_sound.play()
                       
                        
                        if DIALOG_OBJECT[sprite.pos] == str(start_node) :
                            key = DIALOG_OBJECT[sprite.pos]
                            


                        else:
                            key = get_input("Please enter the key :")
                        # try:
                        if key == DIALOG_OBJECT[sprite.pos]:
                            ans=""
                            que = choice(list(QUESTIONS.keys()))
                            ans = get_input(que)
                            if(ans==None):
                                print('ffffffffffffffffffff')
                                ans=""
                            if ans.lower() == QUESTIONS[que].lower():
                                if(int(key) == node_traversal_longest_shortest_path[-1]):
                                    self.score += 100

                                    if self.score == self.max_score :
                                        show(f'Congratulations!! you won with maximum score possible')
                                    else :
                                        show(f'You won. you could have scored {self.max_score - self.score} more.')

                                    # self.death_sound.play()
                                    main_sound.fadeout(3)
                                    self.mario_win.play()
                                    time.sleep(8)
                                    
                                    exit()

                                else:
                                    show(f'Your ans is correct \n{node_traversal_longest_shortest_path[node_traversal_longest_shortest_path.index(int(key))+1]} is your next target ')
                                    self.score += 100

                                    self.keyy = {node_traversal_longest_shortest_path[node_traversal_longest_shortest_path.index(int(key))+1]}
                            else:
                                self.wrong_ans+=1
                                self.score -= 50

                                if self.wrong_ans >=5 :
                                    alpha = self.wave_value()
                                    show('GAME OVER')
                                    main_sound.fadeout(2)
                                    self.game_over.play(6)
                                    time.sleep(6)
                                    exit()
                                show('Your ans is incorrect')
                        else:
                            show('Enter a valid key.')
        
    def cooldowns(self):
        current_time = pg.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]
        self.rect  =self.image.get_rect(center =  self.hitbox.center)

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)