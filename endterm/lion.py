import pygame
import random
 
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Burger(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()


class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image.fill(pygame.Color('red'))
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)
 
    def update(self):
        self.rect.y += 1
        if self.rect.y > 410:
            self.reset_pos()

class Alien(Burger):
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
 
pygame.init()

burger_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
 
for i in range(20):
    burger = Burger('food.png')
    burger.rect.x = random.randrange(screen_width)
    burger.rect.y = random.randrange(screen_height)
    burger_list.add(burger)
    all_sprites_list.add(burger)

for i in range(50):
    block = Block()
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    block_list.add(block)
    all_sprites_list.add(block)
 
alien = Alien('alien.jpg')
all_sprites_list.add(alien)
 
done = False

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
score = 0
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(WHITE)
    all_sprites_list.update()
    burgers_hit_list = pygame.sprite.spritecollide(alien, burger_list, True)
    block_hit_list = pygame.sprite.spritecollide(alien, block_list, True)
 
    for burger in burgers_hit_list:
        score += 1
 
    for block in block_hit_list:
        score -= 1
 
        block.reset_pos()
 
    all_sprites_list.draw(screen)
 
    clock.tick(50)

    text = font.render("Score: "+str(score), True, BLACK)
    screen.blit(text, [10, 10])
 
    pygame.display.flip()

pygame.quit()