import pygame
from random import randrange
import sys
import time
import pygame_menu

res = 600
size = 30 

pygame.init()
screen = pygame.display.set_mode((res, res))
clock = pygame.time.Clock()
pygame.display.set_caption("жуланчик")
font_score = pygame.font.SysFont('Arial', 26, bold = True)
font_end = pygame.font.SysFont('Arial', 50, bold = True)
bg_intro = pygame.image.load('intro.jpg')

def start_the_game(): 
    x, y = randrange(size, res-size, size), randrange(size, res-size, size)
    food = randrange(size, res-size, size), randrange(size, res-size, size)
    length = 1
    snake = [(x, y)]
    dx, dy = 0, 0
    score = 0
    fps = 6

    green = (124, 252, 0)
    red = (255, 0, 0)
    coral = (255, 127, 80)
    gray = (96, 96, 96)

    running = True

    while running:
        screen.fill(pygame.Color('white'))

        #drawing snack and food
        for i in snake:
            pygame.draw.rect(screen, green, (i[0], i[1], size - 2, size - 2))
        screen.blit(pygame.image.load('food.png'), (food[0], food[1]))
        
        #рамки и стены
        pygame.draw.line(screen, gray, (590, 0), (590, 600), 40)
        pygame.draw.line(screen, gray, (10, 0), (10, 590 ), 40)
        pygame.draw.line(screen, gray, (0, 10), (590, 10 ), 40)
        pygame.draw.line(screen, gray, (0, 590), (600, 590), 40)
        
        #show score
        render_score = font_score.render(f'SCORE: {score}', 1, coral)
        screen.blit(render_score, (5, 5))

        #snake movement
        x += dx * size
        y += dy * size
        snake.append((x, y))
        snake = snake[-length:]

        #eating food
        if snake[-1] == food:
            food = randrange(size, res-size, size), randrange(size,res-size, size)
            length += 1
            score += 1
            if length % 3 == 0:
                fps += 1 
        

        #game over 
        if x < size or x == res - size or y < size or y == res - size or len(snake) != len(set(snake)):
            menu = True
            while menu:
                render_end = font_end.render('GAME OVER', 1, coral)
                render_main_menu = font_score.render('MAIN MENU', 1, pygame.Color('black'))
                screen.blit(render_main_menu, (240, 470))
                screen.blit(render_end, (res // 2 - 150, res // 3))
                pygame.display.flip()
                for event in pygame.event.get():
                    mx, my = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and mx >= 240 and my >= 470\
                                                            and mx <= 360 and my <= 550:
                        menu = False
                        running = False
                
        
        pygame.display.flip()
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RIGHT:
                    dx, dy = 1, 0
                if event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                if event.key == pygame.K_DOWN:
                    dx, dy = 0, 1

menu = pygame_menu.Menu('Welcome',220, 300,  theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='player 1')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

while True:

    screen.blit(bg_intro, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()