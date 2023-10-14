from pygame import *
mixer.init()

window = display.set_mode((700, 500))
display.set_caption("Лабиринт")
background = transform.scale(image.load("background.jpg"), (800,600))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 635:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

clock = time.Clock()
FPS = 60

mixer.init()
mixer = mixer.SysFont("Ememy", 20)
text = mixer.render('YOU WIN!', True)

mixer.music.load('les-zvuki-lesa.ogg')
mixer.music.play()
mixer.music.load('zvuk-vyibivaniya-monetyi-iz-igryi-super-mario-30119.ogg')

player = Player(('princess.png'), 10, 10, 10)
enemy = Enemy(('goblin.png'), 470, 300, 5)
gold = GameSprite(('knight.png'), 570, 400, 0)

w1 = Wall(228, 288, 288, 100, 100, 100, 100)
rect = w1.get_rect()

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        enemy.update()

        player.reset()
        enemy.rect()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()

    if sprite.collide_rect(player, monster) or sprite.collide_rect(play, w1) or sprite.collide_rect(play, w2) or sprite.collide_rect(play, w3):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()

    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200,200))
        money.play()

    window.blit(background, (0, 0))
    player.update()
    player.reset()
    enemy.update()
    enemy.reset()
    gold.reset()
    clock.tick(FPS)
    display.update()



'''
import pygame 
import random
import PIL

Pink = (221, 160, 221)
White = (225, 225, 225)
Blue = (29, 32, 76)

FPS = 30

screen = pygame.display.set_mode((800,600))
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
         


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, img='i.png'):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.change_x = 0
        self.change_y = 0
        self.walls = None

        self.coins = None
        self.collected_coins = 0

        self.enemies = pygame.sprite.Group()

        self.alive = True

def update(self):
    self.rect.x += self.change_x

    block_hit_list = pygame.sprite.spiritecollide(self, self.walls, False)
    for bloks in block_hit_list:
        if self.change_x > 0:
            self.rect.right = block.rect.left
        else:
            self.rect.left = block.rect.right

    self.rect.y += self.change_y

    block_hit_list = pygame.sprite.spiritecollide(self, self.walls, False)

    for block in block_hit_list:

        if self.change_y > 0:
            self.rect.bottom = block.rect.top
        else:
            self.rect.top = block.rect.bottem

    coins_hit_list = pygame.sprite.spiritecollide(self, self.walls, False)
    for coin in coins_hit_list:
        self.collected_coins += 1
        coins.kill()

    if pygame.sprite.spiritecollide(self, self.walls, False):
        self.alive = False


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(Blue)

        self.rect = self.image.get_rect()
        self.rect.y = y 
        self.rect.x = x 
    

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, img="princess.png"):
        super(). __init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, img="goblin.png"):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 

        self.start = x 
        self.stop = x + randome.randint(180, 240)
        self.direction = 1

    def update(self):
        if self.rect.x >= self.stop:
            self.rect.x = self.stop
            self.direction = -1
        if self.rect.x <= self.start:
            self.rect.x = self.start
            self.direction = 1
        self.rect.x += self.direction * 2

#pygame.init()
#screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
#pygame.display.set_mode('main')
#pygame.init()
#screen = pygame.display.set_mode(800, 600)
#screen.fill(0, 0, 0)
#pygame.display.flip()

all_sprite_lite = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

wall_coords = [
    [0, 0, 10, 600],
    [790, 0, 10, 600],
    [10, 0, 790, 10],
    [0, 200, 100, 10],
    [0, 590, 600, 10],
    [450, 400, 10, 200],
    [550, 450, 250, 10]
]
#for coord in wall_coords:
 #   walls =Wall(coord[0], coord[1], coord[2], coord[3])
  #  wall_list.add(wall)
   # all_sprite_lite.add(wall)

coins_list = pygame.srite.Group()
coins_coord = [[100, 140], [236, 50], [400, 234]]

for coord in coins_coord:
    coin = Coin(coord[0], coord[1])
    coins_list.add(coin)
    all_sprite_lite.add(coin)


enemies_list = pygame.sprite.Group()
enemies_coord = [[10, 500], [400, 50]]
for coord in enemies_coord:
    enemy = Enemy(coord[0], coord[1])
    enemies_list.add(enemy)
    all_sprite_lite.add(enemy)

player = Player(50, 50)
player.walls = wall_list
all_sprite_lite.add(player)

player.coins = coins_list

player.enemies = enemies_list

font = pygame.font.SysFont('Arial', 24, True)
text = font.render('Игра Окончена', True, WHITE)
text_vin = font.render('Legends of Keokse', True, WHITE)

clock = pygame.teme.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_x = -3
            elif event.key == pygame.K_RIGHT:
                player.change_x = 3
            elif event.key == pygame.K_UP:
                player.change_x = -3
            elif event.key == pygame.K_DOWN:
                player.change_x = 3
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.change_x = 0
            elif event.key == pygame.K_RIGHT:
                player.change_x = 0
            elif event.key == pygame.K_UP:
                player.change_x = 0
            elif event.key == pygame.K_DOWN:
                player.change_x = 0

    screen.fill(PINK)


    if not player.alive:
        screen.blit(text, (100, 100))
    else:
        all_sprite_lite.update()
        all_sprite_lite.draw(screen)

    pygame.display.flip()
    clock.tick(60)

screen.fill((255,255,255))
pygame.display.update()
pygame.quit()

'''