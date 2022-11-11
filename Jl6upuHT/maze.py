#створи гру "Лабіринт"!
import pygame
import os
import time
pygame.init()

# PAHT = os.path.dirname(__file__) + os.sep
PAHT = ""
#===============================================
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, w,h, x,y, speed):
        super().__init__()
        self.image = image
        self.speed = speed
        self.sprite = ""
        self.rect = pygame.Rect(x,y, w,h)
        
    def create(self):
        self.sprite = pygame.transform.scale(pygame.image.load(self.image), (self.rect.w, self.rect.h))
    def show(self):
        wind.blit(self.sprite, (self.rect.x, self.rect.y))
#===============================================
class Hero(GameSprite):
    def __init__(self, image, w,h, x,y, speed):
        super().__init__(image, w,h, x,y, speed)
    def wasd(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] == True:
            self.rect.x -= 7
        if keys[pygame.K_RIGHT] == True:
            self.rect.x += 7
        if keys[pygame.K_DOWN] == True:
            self.rect.y += 7
        if keys[pygame.K_UP] == True:
            self.rect.y -= 7
#===============================================
class Cyborg(GameSprite):
    def __init__(self, image, w,h, x,y, speed):
        super().__init__(image, w,h, x,y, speed)
        self.burder_left = self.rect.x - 230
        self.burder_right = self.rect.x + 50
        self.diraction = 5
    def enemy_move(self):
        if self.rect.x <= self.burder_left or self.rect.x >= self.burder_right:
            self.diraction *= -1
        self.rect.x += self.diraction
#===============================================
class Treasure(GameSprite):
    def __init__(self, image, w,h, x,y, speed):
        super().__init__(image, w,h, x,y, speed)
#===============================================
class Wall(GameSprite):
    def __init__(self, image, w,h, x,y, speed):
        super().__init__(image, w,h, x,y, speed)
        self.sprite = pygame.Surface((w,h))
        self.sprite.fill((249,255,78))
        self.image = self.sprite
    def draw_wall(self):
        wind.blit(self.sprite, (self.rect.x, self.rect.y))#rgb(249,255,78)
#=============================================== 
wind = pygame.display.set_mode((1000, 700))

bg = pygame.transform.scale(pygame.image.load(PAHT + "background.jpg"),(1000,700))

you = Hero(PAHT + "hero.png", 70,70, 100,300, 10)
you.create()
#===============================================
walls = [ 
    Wall('', 110,10, 230,280, 0),
    Wall('', 200,10, 230,380, 0),
    Wall('', 10,250, 330,30, 0),
    Wall('', 10,265, 430,125, 0),
    Wall('', 600,10, 330,30, 0),
    Wall('', 10,210, 230,380, 0),
    Wall('', 200,10, 230,590, 0),
    Wall('', 10,560, 530,30, 0),
    Wall('', 10,200, 430,490, 0),
    Wall('', 100,10, 330,490, 0),
    Wall('', 200,10, 430,690, 0),
    Wall('', 10,510, 630,230, 0),
    Wall('', 110,10, 530,130, 0),
    Wall('', 200,10, 630,230, 0),
    Wall('', 10,100, 730,30, 0),
    Wall('', 10,200, 830,130, 0),
    Wall('', 10,300, 930,30, 0)
    ]
#===============================================
enemy = Cyborg(PAHT + 'cyborg.png', 70,70, 880,400, 10)
enemy.create()

golg = Treasure(PAHT + 'treasure.png', 60,60, 860,600, 0)
golg.create()

pygame.mixer.music.load(PAHT + 'jungles.ogg')
pygame.mixer.music.play()
#===============================================
group = pygame.sprite.Group()
group.add(walls)

nice_cock = pygame.time.Clock()
#===============================================
game = True
while game:
    wind.blit(bg, (0,0))

    you.show()
    you.wasd()

    enemy.show()
    enemy.enemy_move()

    golg.show()

    group.draw(wind)

    if pygame.sprite.spritecollide(you, group, False):
        game = False
    if pygame.sprite.collide_rect(you, golg):
        game = False
    if pygame.sprite.collide_rect(you, enemy):
        game = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    nice_cock.tick(30)

    pygame.display.update()