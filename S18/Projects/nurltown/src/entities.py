import pygame as pg
import config as cfg
import random as rd
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
        self.image = image

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        # Set the initial position
        self.rect.x = init_x
        self.rect.y = init_y

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



class Nurlet(Entity):
    """
    Class representing the inhabitant of Nurltown.
    """
    def __init__(self, init_x = 0, init_y = 0):
        # Load the image to represent the entity
        sprite = pg.image.load("nurlet.png")

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


    def move(self, x, y):
        self.rect.move_ip(x, y)


class Food(Entity):
    """
    Class representing a morsel of food found within Nurltown
    """
    def __init__(self, init_x = 0, init_y = 0):
        # Load the image to represent the entity
        sprite = pg.image.load("jelly.png")

        # Call the parent class constructor
        super(Food, self).__init__(sprite, init_x, init_y)

