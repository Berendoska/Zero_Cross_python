import pygame
import random

pygame.init() #инициализируем pygame
pygame.mixer.init()

def draw(scr):
    pygame.draw.line(scr, (0,0,0), (100,0),(100,300),3)
    pygame.draw.line(scr, (0,0,0), (200,0),(200,300),3)
    pygame.draw.line(scr, (0,0,0), (0,100),(300,100),3)
    pygame.draw.line(scr, (0,0,0), (0,200),(300,200),3)

def draw_x_y(scr, items):
    for i in range(3):
        for j in range(3):
            if items[i][j] == '0':
                pygame.draw.circle(scr, (235,245,255), (j*100 +50, i*100 +50 ),35 )
            elif items[i][j] == 'x':
                pygame.draw.line(scr, (0,50,0),(j*100 +5, i*100 +5 ),(j*100 +95, i*100 +95 ),3)
                pygame.draw.line(scr, (0,50,0),(j*100 +95, i*100 +5 ),(j*100 +5, i*100 +95 ),3)

def win(field, symbol):
    flag_win = False
    for line in field:
        if line.count(symbol) == 3:
            flag_win = True
    for i in range(3):
        if field[0][i] == field[1][i] ==field[2][i] == symbol: 
            flag_win = True
    if field[0][0] ==  field[1][1] == field[2][2] == symbol:
            flag_win = True
    if field[0][2] ==  field[1][1] == field[2][0] == symbol:
            flag_win = True
    return flag_win





SCREEN_SIZE = (300,300) #переменная храния размера экрана
FPS = 30
WHITE = (255,255,255)
moon_glow = ((235,245,255))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
lime = ((180,255,100))

screen = pygame.display.set_mode(SCREEN_SIZE)


pygame.display.set_caption("zero and crosses") #устанавливаем название игры
clock = pygame.time.Clock()
screen.fill((lime))



field = [["","",""], #переменная для хранения каждой клетке на поле
         ["","",""],
         ["","",""]]

run = True
game_over = False

while run:
    clock.tick(FPS)
    for event in pygame.event.get(): #перебераем все события, которые произвел игрок
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            if field[pos[1] // 100][pos[0] // 100] == "":
                field[pos[1] // 100][pos[0] //100] = 'x'
                x,y = random.randint(0,2), random.randint(0,2) #в переменных генерируем значения от 0 до 2
                while field[x][y] != "":
                     x,y = random.randint(0,2), random.randint(0,2)
                field[x][y] = '0'

            winner = win(field, 'x')
            t_winner = win(field, '0')
            if winner or t_winner:
                game_over = True
                if winner:
                    pygame.display.set_caption('Ты чемпион')
                else:
                    pygame.display.set_caption("Победил ИИ")
            elif field[0].count('x') + field[0].count('0') + field[1].count('x') + \
                    field[1].count('0') + field[2].count('x') + field[2].count('0') == 8:
                game_over = True
                pygame.display.set_caption('Победила дружба')



    draw_x_y(screen, field)
    draw(screen)

    screen.blit(screen, (0,0))
    pygame.display.update()

    




