import pygame
import random
import Globals

name = input("Your name\n")
col = input("Choose snake color: 1)Red\n                    2)Black\n                    3)Blue\n")
if col == "Red":
   cl = Globals.Color.red
elif col == "Black":
    cl = Globals.Color.black
elif col == "Blue":
    cl = Globals.Color.blue

pygame.init()

dis = pygame.display.set_mode((Globals.Global.width, Globals.Global.height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

font_style = pygame.font.SysFont("Dubai", 40)
font_score = pygame.font.SysFont("Dubai", 25)


def message(msg, color):
    mes = font_style.render(msg, True, color)
    dis.blit(mes, [Globals.Global.width / 6, Globals.Global.height / 3])


def game():
    result = open("score.txt", "a")
    global name
    global cl
    Key = {'W': True, 'A': True, 'S': True, 'D': True}
    only_one = True
    game_over = False
    game_close = False
    X, Y = 0, 0
    x, y = random.randrange(0, Globals.Global.width, Globals.Global.size), random.randrange(0, Globals.Global.height,
                                                                                            Globals.Global.size)
    apple = random.randrange(0, Globals.Global.width, Globals.Global.size), random.randrange(0, Globals.Global.height,
                                                                                             Globals.Global.size)
    snake = [(x, y)]
    snake_len = 1
    speed = 7
    score = 0
    Level = 1

    while not game_over:

        while game_close:
            dis.fill(Globals.Color.yellow)
            m = "Game Over, " + name
            message(m, Globals.Color.black)
            keyboard = font_score.render("Press C to play again, Q to quit or R to save result", True, Globals.Color.black)
            dis.blit(keyboard, (300, 500))
            render_score = font_score.render(f'Score: {score}', True, Globals.Color.blue)
            dis.blit(render_score, (5, 5))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()
                    if event.key == pygame.K_r and only_one:
                        resultat = name + ": " + str(score) + " points\n"
                        result.write(resultat)
                        only_one = False
                if event.type == pygame.QUIT:
                    exit()

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

        if x < 0 or x > Globals.Global.width - Globals.Global.size + 1 or y < 0 or y > Globals.Global.height - Globals.Global.size + 1 or len(
                snake) != len(set(snake)):
            game_close = True

        dis.fill(Globals.Color.yellow)
        [(pygame.draw.rect(dis, cl, (i, j, Globals.Global.size - 2, Globals.Global.size - 2))) for i, j in snake]

        if score % 7 == 0 and score != 0:
            pygame.draw.rect(dis, Globals.Color.gold, (*apple, Globals.Global.size, Globals.Global.size))
        else:
            pygame.draw.rect(dis, Globals.Color.green, (*apple, Globals.Global.size, Globals.Global.size))

        render_score = font_score.render(f'Score: {score}', True, Globals.Color.blue)
        dis.blit(render_score, (5, 5))
        render_Level = font_score.render(f'Level: {Level}', True, Globals.Color.black)
        dis.blit(render_Level, (700, 5))
        x = x + X * Globals.Global.size
        y = y + Y * Globals.Global.size
        snake.append((x, y))
        snake = snake[-snake_len:]
        if snake[-1] == apple:
            apple = random.randrange(0, Globals.Global.width, Globals.Global.size), random.randrange(0,
                                                                                                     Globals.Global.height,
                                                                                                     Globals.Global.size)
            snake_len = snake_len + 1
            speed = speed + 1

            if score % 7 == 0 and score != 0:
                score = score + 2
            else:
                score = score + 1

            if score >= Level * 5 and score != 0:
                Level += 1

        pygame.display.flip()
        clock.tick(speed)


game()
print("Do you want to see the leaderboard? Yes/No")
leaderboard = input()
if leaderboard == "Yes":
    leaderboards = open("score.txt", "r")
    print(leaderboards.read())
else:
    print("Ok")
