import pygame
import random
pygame.init()
width = 800
height = 600
size = 40
snake_len = 1
score = 0
speed = 7

dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

font_style = pygame.font.SysFont("Dubai", 120)
font_score = pygame.font.SysFont("Dubai", 25)
Key = {'W': True, 'A': True, 'S': True, 'D': True}


class Color:
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (255, 0, 00)
    green = (0, 255, 0)
    blue = (50, 153, 213)


def message(msg, color):
    mes = font_style.render(msg, True, color)
    dis.blit(mes, [width / 6, height / 3])


x, y = random.randrange(0, width, size), random.randrange(0, height, size)
apple = random.randrange(0, width, size), random.randrange(0, height, size)
snake = [(x, y)]

X, Y = 0, 0


while True:
    dis.fill(Color.yellow)
    [(pygame.draw.rect(dis, Color.red, (i, j, size - 2, size - 2))) for i, j in snake]
    pygame.draw.rect(dis, Color.green, (*apple, size, size))
    render_score = font_score.render(f'Score: {score}', True, Color.blue)
    dis.blit(render_score, (5, 5))
    x = x + X * size
    y = y + Y * size
    snake.append((x, y))
    snake = snake[-snake_len:]
    if snake[-1] == apple:
        apple = random.randrange(0, width, size), random.randrange(0, height, size)
        snake_len = snake_len + 1
        speed = speed + 1
        score = score + 1

    if x < 0 or x > width - size + 1 or y < 0 or y > height - size + 1 or len(snake) != len(set(snake)):
        while True:
            message("Game Over", Color.black)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if (key[pygame.K_w] or key[pygame.K_UP]) and Key['W']:
        X, Y = 0, -1
        Key = {'W': True, 'A': True, 'S': False, 'D': True}
    if (key[pygame.K_a] or key[pygame.K_LEFT]) and Key['A']:
        X, Y = -1, 0
        Key = {'W': True, 'A': True, 'S': True, 'D': False}
    if (key[pygame.K_s] or key[pygame.K_DOWN]) and Key['S']:
        X, Y = 0, 1
        Key = {'W': False, 'A': True, 'S': True, 'D': True}
    if (key[pygame.K_d] or key[pygame.K_RIGHT]) and Key['D']:
        X, Y = 1, 0
        Key = {'W': True, 'A': False, 'S': True, 'D': True}
