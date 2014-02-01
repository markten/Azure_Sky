import pygame
from constants import *

class Spritesheet():
    
    sprite_sheet = None
    
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
        
    def getImage(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(GREEN)
        
        return image