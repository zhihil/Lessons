# Breathing Life Into Nurltown

In this tutorial, we will be creating the Nurltown ecosystem, and along the way, we will also be exloring the basics
of game development using the Pygame platform. We will be creating a 2D game world, populating it with entities
(nurles and food), and using that to understand some key concepts of game development such as
**the game loop**, **rendering**, and **game logic**.

For this introduction to pygame, we will be roughly following
[this youtube video series by sentdex](https://www.youtube.com/watch?v=ujOTNg17LjI&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO).
As we progress through the components of Pygame, I will be adding further commentary to develop our understanding of
general programming and game development. That said, if you feel confident, definitely use the video series as an
extra resource to enrich your learning.

**NOTE:** Below is a step-by-step development of our understanding of pygame, where we will be discussing small
parts of the entire file at a time.

[**You can find the directory with complete files here**](https://github.com/UWCoffeeNCode/Lessons/blob/master/S18/Projects/nurltown/src).

When all is said and done, we expect our initial pass at the game to look something like this!

![Lesson 3 game teaser](../assets/images/reference/lesson_3_teaser.gif)

## Setting up a game configuration files

We will begin by writing a configuration file for our game. As we are developing the game, we can expect to be tweaking 
the look and behaviour of our game and the entities inside quite a bit! We would not want to be rooting through all of
our files everytime we do that. So, it's generally a good development practice to store most of game configurations and
parameters in one centralized file that all other files import necessary values from.

In the root directory of your project, create a file called `config.py`. Here we will be storing our configurations.
 
While you are at it, create another file and name it `__init__.py`. This can stay blank, but a file with that name needs
to exist in any directory we want python to recognize as an importable module. As we make new folders inside our root
directory, we will continue to add `__init__.py` files in those folders as well.

### `config.py`

```python
"""
config.py
Module containing the configurations for the Nurltown ecosystem simulation
These configurations contain global and default parameters that dictate
the setup of the ecosystem and behaviors of the entities within, such as
nurlets, food, and obstacles
"""

# The game dimensions, as it will appear on your screen
GAME_WIDTH = 900
GAME_HEIGHT = 600

# The dimensions of nurlets
NURLET_WIDTH = 50
NURLET_HEIGHT = 50

# The speed at which the nurlets travel (# of pixels/frame)
NURLET_SPEED = 10

# The maximum angle of deflection from origin during the shuffling animation
NURLET_SHUFFLE_ANGLE = 15

# The maximum number of food entities which can exist at once in the ecosystem
MAX_NUM_FOOD = 10
```

**NOTE:** As we are working through this project, I will highly recommend that you are diligent about the following:
1. Write short descriptions at the top of files outlining its purpose and any special notes about the contents
2. Write meaningful comments beside sections of code about its purpose and justifications for any numbers or formulae used.

You would be surprised how quickly you can forget why you used a particular value or wrote a bit of code just days ago.
Writing meaningful comments not only guards against your human flaws, but it indicates good practice as a software
developer to anyone inspecting your code (potential employers included 😉).

---

We will also create another file in the root directory, and call it `colors.py`. This will be a file where we will
organize all the color descriptions we will be using throughout the game.

### `colors.py` 

```python
"""
colors.py
Module containing the standard descriptions of the colors used in Nurltown

When the colors are described as a 3-element tuple, it is the RGB description, with
each number representing the amount of intensity in the Red, Blue, Green channel, respectively
"""

red = 255, 0, 0
black = 0, 0, 0
```

## Building the ecosystem

With the configuration files set up, we will now turn out attention to writing the script file `nurltown.py`, which will:
* serve as the entry point to our game (the program to run to start the game)
* manage the game loop

### Learning about Object-Oriented Programming (OOP)
In order to code the bullding blocks of Nurltown, we will employ a method of programming called _Object-Oriented Programming_.
Within this paradigm, we aim to model a set of logically coherent pieces of functionality under the classification of an _Object_.

For instance, each of our nurlets may be considered an Object, and it will possess a set of functionality that you may expect 


---

![Under Construction](http://www.openheavenworshipcenter.com/wp-content/uploads/2017/07/Under-Construction-Sign-for-Locator.png)

_authored by Ahrar Monsur_