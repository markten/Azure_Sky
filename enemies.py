import pygame
from constants import *
import random
from math import sin, cos

class Boss(pygame.sprite.Sprite):
    
    direction = 1
    velocity = 5
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/boss.png").convert()
        self.image.set_colorkey(GREEN)
        self.rect = self.image.get_rect()
        
        self.rect.x = 0
        self.rect.y = 50
        
    def update(self):
        if self.rect.x < 0:
            self.direction = 1
        if self.rect.x > (WINDOW_X_SIZE - self.rect.w):
            self.direction = -1
        self.rect.x += (self.direction * self.velocity)
            
class Bullet(pygame.sprite.Sprite):
    
    age = 0
    x_vect = 0
    y_vect = 0
    
    def __init__(self, x, y, x_vect, y_vect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/bullet.png").convert_alpha()
        self.image.set_colorkey(GREEN)
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.x_vect = x_vect
        self.y_vect = y_vect
        
    def update(self):
        self.age += 1
        self.rect.x += self.x_vect
        self.rect.y += self.y_vect
        
def generate_bullet_cluster(x, y):
    
    velocity = 10
    amount = random.randrange(5, 10)
    d_theta = PI / amount
    
    new_cluster = pygame.sprite.Group()
    
    for bullet in range(amount):
        y_vect = velocity * sin(d_theta * bullet)
        x_vect = velocity * cos(d_theta * bullet)
        newBullet = Bullet(x, y, x_vect, y_vect)
        new_cluster.add(newBullet)
    
    return new_cluster

def generate_bullet_stream(x, y):
    
    velocity = 10
    amount = random.randrange(3, 9)
    
    new_stream = pygame.sprite.Group()
    
    for bullet in range(amount):
        x_vect = random.randrange(-2, 2)
        y_vect = random.randrange(5, 10)
        newBullet = Bullet(x, y, x_vect, y_vect)
        new_stream.add(newBullet)
    
    return new_stream