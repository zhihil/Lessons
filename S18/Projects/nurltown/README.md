# Nurltown: an machine learning powered ecosystem simulator

The happy, sunshiney little village of Nurltown, where virtual creatures (nurlets) run around, have outdoor potlucks,
and **fight to the death.**

## Objectives
* Design a 2D game engine to run the simulation
* Develop neural networks to give your nurlet a brain (it’s ALIIIIIVE!!)
* Implement evolutionary algorithms to teach your nurlets how to eat, grow, multiply, and defend against their enemies

### Tools & Components
* python 3
* virtualenv for sandboxing python
* numpy numerical computation package
* scipy library for scientific computing
* pyGame library for game development
* our very own custom NEAT implementation

## Tentative Syllabus
| Lesson # | Week # | Date          | Description                                    |
| :------- | ------ | ------------- | ---------------------------------------------- |
| -        | 4      | May 23, 2018  | Introductions & Sign-ups                       |
| 1        | 5      | May 30, 2018  | Intro to game design, tools & components, and installation of software |
| 2        | 6      | June 6, 2018  | `-- NO LESSON (AHRAR UNAVAILABLE) --`       |
| -        | 7      | June 13, 2018 | `-- NO LESSON (HELL WEEK) --`                  |
| 3        | 8      | June 20, 2018 | Explore pygame and begin building the ecosystem |
| 4        | 9      | June 27, 2018 | -- |
| 5        | 10     | July 4, 2018  | -- |
| 6        | 11     | July 11, 2018 | -- |
| 7        | 12     | July 18, 2018 | -- |
| -        | 13     | July 25, 2018 | -- |

## Installation

### Installing `python3`
#### On Mac OS X


1. First, you must install the Homebrew package manager. Open a terminal and run

`$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

2. Insert the Homebrew directory at the top of your **PATH** environment variable. You can do this by adding
the following line at the bottom of your `~/.profile` file

`export PATH=/usr/local/bin:/usr/local/sbin:$PATH`

3. `brew install python`

Note: The python installation will also use the `pip` python package manager. We will use this to install the python utilities
and libraries that we will need.

### Installing `virtualenv`
1. `pip install --upgrade pip`

