# Glossary

### Game Loop
The game loop is the heart of any game. Fundamentally, it is a function which runs continuously, creating the game frame-by-frame.

In each loop, there are has different phases, each modifying the game in a special way. The phases are **initialization**,
**updating**, and **drawing**.

1. **Initialization:** In this phase, game setups (from configuration files) are run, and the environment is prepared for the draw and
update phases. This can include creating the entities (characters and items) and loading the physics engine.
2. **Updating:** During this phase, all the objects in the game are prepared to be drawn. This can include taking in
player inputs and moving the character accordingly. Or, if any combat occurred, the amount of health points remaining 
may need to be adjusted.
3. **Drawing:** All the changes that occur in the updating phase must now be represented visually (or by audio). During
the draw phase, the character is redrawn to a different position, the health bar reflects the change in health, and
the current score is perhaps updated.

![The game loop](http://openbookproject.net/thinkcs/python/english3e/_images/pygame_structure.png)

