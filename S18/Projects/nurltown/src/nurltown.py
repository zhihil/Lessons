# nurltown.py

import sys
import pygame as pg
import config as cfg
import entities as ntts
import random as rd
import colors

from functools import reduce

def main():
    """
    Main game loop
    """

    width, height = cfg.GAME_WIDTH, cfg.GAME_HEIGHT

    pg.init()

    screen = pg.display.set_mode((width, height))
    constrain_within_screen = screen_constraint_generator(screen)

    nurlets = pg.sprite.Group()
    food = pg.sprite.Group()

    nurlet = ntts.Nurlet(width/2, height/2)
    jellies = [ntts.Food(*get_random_pos(screen)) for x in range(cfg.MAX_NUM_FOOD)]

    entity_groups = [food, nurlets]

    nurlets.add(nurlet)
    food.add(jellies)

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

        # Update the nurlets
        for n in nurlets:
            n.update()


        # Redraw the entities
        for group in entity_groups:
            map(constrain_within_screen, group.sprites())
            group.draw(screen)

        pg.display.update()


def screen_constraint_generator(screen):
    """
    A generator function which produces a function which accepts a sprite and constraints it within the
    bounds of the supplied pygame.Display object
    :param screen: A game screen
    :type screen: pygame.Surface
    :return: A function which constrains a sprite to be within a game display
    :rtype: function
    """

    def generated_func(sprite):
        """
        A function which contains a supplied sprite to be within a game display
        :param sprite: A game sprite
        :type sprite: pygame.sprite.Sprite
        :return: None
        """
        sprite.rect.clamp_ip(screen.get_rect())

    return generated_func


def get_random_pos(screen):
    """
    Function with provides a random location within the bounds of a screen
    :param screen: A game screen
    :type screen: pygame.Surface
    :return: An (x, y) coordinate within the screen
    :rtype: tuple
    """

    rect = screen.get_rect()
    x = rd.randint(rect.left, rect.width)
    y = rd.randint(rect.top, rect.height)

    return x, y

if __name__ == "__main__":
    main()
