import pygame as pg
import config as cfg
import random as rd
import colors

class Nurlet(pg.sprite.Sprite):

    def __init__(self, init_x = 0, init_y = 0):
        # Call the parent class (Sprite) constructor
        pg.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pg.Surface([cfg.NURLET_WIDTH, cfg.NURLET_HEIGHT])
        self.image.fill(colors.red)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        # Set the initial position
        self.rect.x = init_x
        self.rect.y = init_y


    def update(self):
        multiplier = 10
        self.rect.x += multiplier * rd.randint(-1, 1)
        self.rect.y += multiplier * rd.randint(-1, 1)

