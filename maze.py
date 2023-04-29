#создай игру "Лабиринт"!
#sprite.collide_rect()
from pygame import *
mixer.init()
font.init()
window = display.set_mode((800,600))
bg = transform.scale(image.load('background.jpg'),(800,600))
display.set_caption('лабиринт')
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')
clock = time.Clock()
font = font.SysFont('Arial',70)
win = font.render('You win',True,(255,50,50))
lose = font.render('You lose',True,(255,50,50))
play = True
fps = 60
walls = list()
end = True
wal = 'o'
class Gamesprite(sprite.Sprite):
    def __init__(self,sprite,speed,player_x,player_y):
        super().__init__()
        self.image = transform.scale(image.load(sprite),(70,70))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Gamesprite):
    def __init__(self,sprite,speed,player_x,player_y):
        super().__init__(sprite,speed,player_x,player_y)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 730:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 530:
            self.rect.y += self.speed
class Bot(Gamesprite):
    def __init__(self,sprite,speed,player_x,player_y,coordinat1,coordinat2,ploskost = None):
        super().__init__(sprite,speed,player_x,player_y)
        self.a = 'left'
        self.coordinat1 = coordinat1
        self.coordinat2 = coordinat2
        self.ploskost = ploskost
    def automove(self):
        if self.ploskost == 'x':
            if self.a == 'left':
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed
            if self.rect.x <= self.coordinat1:
                self.a = 'right'
            if self.rect.x >= self.coordinat2:
                self.a = 'left'
        if self.ploskost == 'y':
            if self.a == 'left':
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed
            if self.rect.y <= self.coordinat1:
                self.a = 'right'
            if self.rect.y >= self.coordinat2:
                self.a = 'left'
class Wall(sprite.Sprite):
    def __init__(self,wight,hight,col1,col2,col3,coordinat_x,coordinat_y):
        super().__init__()
        self.wight = wight
        self.hight = hight
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3
        self.image = Surface((wight,hight))
        self.image.fill((self.col1,self.col2,self.col3))
        self.rect = self.image.get_rect()
        self.rect.x = coordinat_x
        self.rect.y = coordinat_y
    def wall_update(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

player = Player('hero.png',5,0,280)
enemy = Bot('cyborg.png',3,700,430,530,730,'x')
enemy2 = Bot('cyborg.png',5,400,0,0,200,'y')
sokrovishe = Gamesprite('treasure.png',0,700,520)
wall1 = Wall(300,10,120,100,255,0,200)
wall2 = Wall(390,10,120,100,255,0,370)
wall3 = Wall(10,100,120,100,255,380,270)
wall4 = Wall(230,10,120,100,255,390,270)
wall5 = Wall(10,270,120,100,255,290,0)
wall6 = Wall(10,70,120,100,255,150,300)
wall7 = Wall(400,10,120,100,255,300,0)
wall8 = Wall(10,490,120,100,255,530,100)
wall9 = Wall(300,10,120,100,255,530,590)
wall10 = Wall(10,400,120,100,255,700,0)
wall11 = Wall(10,190,120,100,255,790,400)
wall12 = Wall(100,10,120,100,255,700,400)
walls.append(wall1)
walls.append(wall2)
walls.append(wall3)
walls.append(wall4)
walls.append(wall5)
walls.append(wall6)
walls.append(wall7)
walls.append(wall8)
walls.append(wall9)
walls.append(wall10)
walls.append(wall11)
walls.append(wall12)
while play:
    for i in event.get():
        if i.type == QUIT:
            play = False
    if end:
        player.update()
        enemy.automove()
        enemy2.automove()
        window.blit(bg,(0,0))
        player.reset()
        enemy.reset()
        enemy2.reset()
        sokrovishe.reset()
        for i in range(len(walls)):
            walls[i].wall_update()
        for i in range(len(walls)):
            if sprite.collide_rect(player,walls[i]):
                wal = 'a'
        if sprite.collide_rect(player,enemy) or sprite.collide_rect(player,enemy2) or wal == 'a':
            end = False
            wal = 'o'
            window.blit(lose,(300,300))
            kick.play()
        if sprite.collide_rect(player,sokrovishe):
            end = False
            window.blit(win,(300,300))
            money.play()
        display.update()
        clock.tick(fps)
    else:
        end = False