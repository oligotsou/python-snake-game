import pygame
import random
import sys

pygame.init()

# Screen size
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Colors
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)

snake_block = 10
snake_speed = 15

font = pygame.font.SysFont(None,35)

def draw_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], block, block])

def message(msg,color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [WIDTH/6, HEIGHT/3])

def game_loop():

    game_over = False
    game_close = False

    x = WIDTH/2
    y = HEIGHT/2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, WIDTH-snake_block)/10.0)*10.0
    foody = round(random.randrange(0, HEIGHT-snake_block)/10.0)*10.0

    while not game_over:

        while game_close == True:
            screen.fill(black)
            message("Game Over! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        x += x_change
        y += y_change

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        screen.fill(black)

        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, WIDTH-snake_block)/10.0)*10.0
            foody = round(random.randrange(0, HEIGHT-snake_block)/10.0)*10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

game_loop()
