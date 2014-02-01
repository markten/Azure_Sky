import pygame
from constants import *
from spritesheets import Spritesheet

class Player(pygame.sprite.Sprite):
    
    # Movement
    velocity = 15
    direction = 0
    
    # Animation
    frames = []
    frame_index = 0
    
    # Stats
    max_hitpoints = 3
    current_hitpoints = 3
    max_shields = 2
    current_shields = 2
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = Spritesheet("sprites/player.png")
        image = sprite_sheet.getImage(   0,   0, 72, 72)
        self.frames.append(image)
        image = sprite_sheet.getImage( 72,   0, 72, 72)
        self.frames.append(image)
        image = sprite_sheet.getImage( 2*72,   0, 72, 72)
        self.frames.append(image)
        image = sprite_sheet.getImage( 3*72,   0, 72, 72)
        self.frames.append(image)
        
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        
        self.rect.x = 0
        self.rect.y = WINDOW_Y_SIZE - self.rect.h
    
    def set_velocity(self, velocity):
        self.current_velocity = velocity
        
    def damage(self):
        if self.current_shields > 0:
            self.current_shields -= 1
            return SHIELD_DAMAGE
        elif self.current_hitpoints > 0:
            self.current_hitpoints -= 1
            return HP_DAMAGE
        else:
            return DEATH
            
    def reset(self):
        self.current_shields = self.max_shields
        self.current_hitpoints = self.max_hitpoints
        
    def update(self):
        if self.direction == -1 and self.rect.x > 0:
            self.rect.x -= self.velocity
        if self.direction == 1 and self.rect.x < (WINDOW_X_SIZE - self.rect.w):
            self.rect.x += self.velocity
        if self.frame_index == 3:
            self.frame_index = 0
        else:
            self.frame_index += 1
            
        self.image = self.frames[self.frame_index]
       