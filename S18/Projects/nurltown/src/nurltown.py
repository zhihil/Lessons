# nurltown.py

import sys
import pygame as pg
import config as cfg
import entities as ntt
import colors

width, height = cfg.GAME_WIDTH, cfg.GAME_HEIGHT

pg.init()
screen = pg.display.set_mode((width, height))

nurlet = ntt.Nurlet(width/2, height/2)
entities = pg.sprite.Group()
entities.add(nurlet)

while True:

    # Handle the events that the game instance encounters
    # Events can be mouse movements/clicks, key presses, window resizing, joystick use, etc.
    # You can read more about the supported event types here:
    # https://www.pg.org/docs/ref/event.html
    for event in pg.event.get():

        # Quit the game and program when the 'x' button on the window is pressed
        if event.type == pg.QUIT: sys.exit()
        # Adds a quick way to exit the game by press the ';' button
        if event.type == pg.KEYDOWN and event.key == pg.K_SEMICOLON: sys.exit()

    # Clear the screen
    screen.fill(colors.black)

    # Draw entities
    for e in entities:
        e.update()
        e.rect.clamp_ip(screen.get_rect())
        screen.blit(e.image, e.rect)

    pg.display.update()


