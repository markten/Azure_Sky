import pygame

### Define Color Constants
BLACK   = (   0,   0,   0)
WHITE   = ( 255, 255, 255)
RED     = ( 255,   0,   0)
GREEN   = (   0, 255,   0)
BLUE    = (   0,   0, 255)
AZURE   = (   0, 127, 255)
GRAY    = ( 192, 192, 192)

### Define view name constants
MENU_VIEW = 0
GAME_VIEW = 1
WINDOW_X_SIZE = 800
WINDOW_Y_SIZE = 600

MAX_BULLET_AGE = 150

### Damage Types
NONE = 0
HP_DAMAGE = 1
SHIELD_DAMAGE = 2
DEATH = 3

### Math constants
PI = 3.14

### Timer constants
STREAM_TIMER = pygame.USEREVENT+1
CLUSTER_TIMER = pygame.USEREVENT+2