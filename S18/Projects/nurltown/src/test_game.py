# test_game.py

import sys, pygame
pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("supreme_leader2.png")
ballrect = ball.get_rect()
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Game Development In Progress...', False, (255, 0, 0))
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(textsurface,(175,500))
    pygame.display.update()