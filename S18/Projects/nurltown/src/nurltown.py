# nurltown.py


# Importing external modules.
# Some of the statements have the form 'import [THIS] as [THAT]', which just allows as to use
# a shorter alias (alternate name to target the module) to reduce the amount we have to type
import sys                      # Allows access to information about the computer, its filesystem, etc
import pygame as pg             # The Pygame module
import config as cfg            # The configuration file containing parameters about the game
import entities as ntts         # Module containing the classes for the objects that will populate the game
import random as rd             # Module which has useful functions involving random numbers
import colors                   # Imports variables describing colors

def main():
    """
    This is the entry point in to the Nurltown ecosystem simulator. The function does the following:
    1. Instantiates a Pygame session
    2. Set the game configuration and utilities
    3. Populates the ecosystem with an initial collection of nurlets and food
    4. Continuously runs a loop of updating the states of the game entities and redrawing the game state
    """

    width, height = cfg.GAME_WIDTH, cfg.GAME_HEIGHT

    pg.init()

    screen = pg.display.set_mode((width, height))
    constrain_within_screen = screen_constraint_generator(screen)
    get_random_pos = random_pos_generator(screen)

    nurlets = pg.sprite.Group()
    food = pg.sprite.Group()

    nurlet = ntts.Nurlet(width/2, height/2)
    jellies = [ntts.Food(*get_random_pos()) for x in range(cfg.MAX_NUM_FOOD)]

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
        nurlets.update(food)

        # Replenish food
        num_to_respawn = max(0, cfg.MAX_NUM_FOOD - len(food))
        if num_to_respawn: food.add(ntts.Food(*get_random_pos()))


        # Redraw the entities
        for group in entity_groups:
            for sprite in group.sprites():
                constrain_within_screen(sprite)
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
        """
        sprite.rect.clamp_ip(screen.get_rect())

    return generated_func


def random_pos_generator(screen):
    """
    A generator Function which produces a function which returns a random location within the bounds of a supplied screen
    :param screen: A game screen
    :type screen: pygame.Surface
    :return: A function which provides a random location within the bounds of a supplied screen
    :rtype: function
    """

    def generated_func():
        """
        A function which provides a random location within the bounds of a supplied screen
        :return: An (x, y) coordinate within the screen
        :rtype: tuple[int]
        """

        rect = screen.get_rect()
        x = rd.randint(rect.left, rect.width)
        y = rd.randint(rect.top, rect.height)

        return x, y

    return generated_func


# This code block ensures that the main() function (the entry point to the game) only runs if this script
# file is run directly, and not imported as a module.
if __name__ == "__main__":
    main()
