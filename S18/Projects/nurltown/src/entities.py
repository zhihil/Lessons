import pygame as pg
import config as cfg
import random as rd
import itertools as itt
import numpy as np
import math
import colors

class Entity(pg.sprite.Sprite):
    """
    A base class for an entity in Nurltown
    """

    def __init__(self, image, init_x = 0, init_y = 0):
        # Call the parent class (Sprite) constructor
        pg.sprite.Sprite.__init__(self)

        # Set the sprite for the entity
        self.original_image = image
        self.image = image

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        # Set the initial position
        self.rect.x = init_x
        self.rect.y = init_y
        self.shuffle_cycle = self.generate_shuffle_frames(cfg.NURLET_SHUFFLE_ANGLE)

    def generate_shuffle_frames(self, max_deflection):
        half_set = list(np.linspace(-1*max_deflection, max_deflection, 20))
        full_set =  half_set[::-1]+ half_set
        return itt.cycle(full_set)

    def distance_to(self, other):
        my = self.rect
        its = other.rect
        dist = math.sqrt((its.x - my.x)**2 + (its.y - my.y)**2)
        return dist

    def unit_vector_to(self, other):
        my = self.rect
        its = other.rect
        dist = self.distance_to(other)
        xhat = (its.x - my.x)/dist
        yhat = (its.y - my.y)/dist
        return xhat, yhat

    def shuffle_sprite(self):
        self.image = pg.transform.rotate(self.original_image, next(self.shuffle_cycle))

    def move(self, x, y):
        # self.image = pg.transform.rotate(self.original_image, rd.randint(-20, 20))
        self.shuffle_sprite()
        self.rect.move_ip(x, y)



class Nurlet(Entity):
    """
    Class representing the inhabitant of Nurltown.
    """
    def __init__(self, init_x = 0, init_y = 0):
        # Load the image to represent the entity
        # sprite = pg.image.load("nurlet.png")
        sprite = pg.image.load("supreme_leader3.png")

        # Call the parent class constructor
        super(Nurlet, self).__init__(sprite, init_x, init_y)
        self.speed = cfg.NURLET_SPEED

    def update(self, food):
        self.seek_closest(food)
        self.eat_nearby(food)

    def seek_closest(self, group):
        # Initialize variables for closest food
        closest_distance = math.inf
        closest_entity = None


        # Find the closest food
        for entity in group:
            dist = self.distance_to(entity)
            if dist < closest_distance:
                closest_distance = dist
                closest_entity = entity

        # Move towards the closest food at maximum speed
        x, y = [self.speed * i for i in self.unit_vector_to(closest_entity)]
        self.move(x, y)

    def eat_nearby(self, food):
        pg.sprite.spritecollide(self, food, True)




class Food(Entity):
    """
    Class representing a morsel of food found within Nurltown
    """
    def __init__(self, init_x = 0, init_y = 0):
        # Load the image to represent the entity
        # sprite = pg.image.load("jelly.png")
        sprite = pg.image.load("kimbap copy.png")

        # Call the parent class constructor
        super(Food, self).__init__(sprite, init_x, init_y)

