import pygame
from random import choice


WIDTH, HEIGHT = 750, 750
TILE = 50
GREEN = (0, 255, 0)

cols = (WIDTH // TILE + 1) // 2
rows = (HEIGHT // TILE + 1) // 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze example")
clock = pygame.time.Clock()
FPS = 60


class Cell:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
		self.visited = False

	def draw(self):
		x = 2 * self.x * TILE
		y = 2 * self.y * TILE

		if self.visited:
			pygame.draw.rect(screen, pygame.Color('red'), (x, y, TILE, TILE))

		if not self.walls['top']:
			pygame.draw.rect(screen, pygame.Color('red'), (x, y - TILE, TILE, TILE))
		if not self.walls['right']:
			pygame.draw.rect(screen, pygame.Color('red'), (x + TILE, y, TILE, TILE))
		if not self.walls['bottom']:
			pygame.draw.rect(screen, pygame.Color('red'), (x, y + TILE, TILE, TILE))
		if not self.walls['left']:
			pygame.draw.rect(screen, pygame.Color('red'), (x - TILE, y, TILE, TILE))

	def check_cell(self, x, y):
		if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
			return False
		return grid_cell[x + y * cols]

	def check_neighbours(self):
		neighbours = []

		top = self.check_cell(self.x, self.y - 1)
		right = self.check_cell(self.x + 1, self.y)
		bottom = self.check_cell(self.x, self.y + 1)
		left = self.check_cell(self.x - 1, self.y)

		if top and not top.visited:
			neighbours.append(top)
		if right and not right.visited:
			neighbours.append(right)
		if bottom and not bottom.visited:
			neighbours.append(bottom)
		if left and not left.visited:
			neighbours.append(left)

		return choice(neighbours) if neighbours else False


def remove_walls(current_cell, next_cell):
	dx = current_cell.x - next_cell.x
	dy = current_cell.y - next_cell.y

	if dx == 1:
		current_cell.walls['left'] = False
		next_cell.walls['right'] = False
	if dx == -1:
		current_cell.walls['right'] = False
		next_cell.walls['left'] = False
	if dy == 1:
		current_cell.walls['top'] = False
		next_cell.walls['bottom'] = False
	if dy == -1:
		current_cell.walls['bottom'] = False
		next_cell.walls['top'] = False

def check_wall(grid_cell, x, y):
	if x % 2 == 0 and y % 2 == 0:
		return False
	if x % 2 == 1 and y % 2 == 1:
		return True

	if x % 2 == 0:
		grid_x = x // 2
		grid_y = (y - 1) // 2
		return grid_cell[grid_x + grid_y * cols].walls['bottom']
	else:
		grid_x = (x - 1) // 2
		grid_y = y // 2
		return grid_cell[grid_x + grid_y * cols].walls['right']

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False

grid_cell = [Cell(x, y) for y in range(rows) for x in range(cols)]
current_cell = grid_cell[0]
current_cell.visited = True
stack = []



all_sprites.update()
pygame.display.flip()
clock.tick(30)
pygame.quit()