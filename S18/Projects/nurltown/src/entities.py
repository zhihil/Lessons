import pygame as pg
import config as cfg
import random as rd
import colors

class Entity(pg.sprite.Sprite):
    """
    A base class for an entity in Nurltown
    """

    def __init__(self, image, init_x = 0, init_y = 0):
        # Call the parent class (Sprite) constructor
        pg.sprite.Sprite.__init__(self)

        # Set the sprite for the entity
        self.image = image

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        # Set the initial position
        self.rect.x = init_x
        self.rect.y = init_y

class Nurlet(Entity):
    """
    Class representing the inhabitant of Nurltown.
    """
    def __init__(self, init_x = 0, init_y = 0):
        # Load the image to represent the entity
        sprite = pg.image.load("nurlet.png")

        # Call the parent class constructor
        super(Nurlet, self).__init__(sprite, init_x, init_y)

    def update(self):
        multiplier = 10
        self.rect.x += multiplier * rd.randint(-1, 1)
        self.rect.y += multiplier * rd.randint(-1, 1)


class Food(Entity):
    """
    Class representing a morsel of food found within Nurltown
    """
    def __init__(self, init_x = 0, init_y = 0):
        # Load the image to represent the entity
        sprite = pg.image.load("jelly.png")

        # Call the parent class constructor
        super(Food, self).__init__(sprite, init_x, init_y)

