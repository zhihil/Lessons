# 

## Game Loop [1]



## Finite-State Machine [2]

![wikipedia, finite-state machine](https://upload.wikimedia.org/wikipedia/commons/9/9e/Turnstile_state_machine_colored.svg)

A finite-state machine (FSM) is an abstract machine that can be in only 1 of a finite number of states at any moment. The two states in the turnstile example are "locked" and "unlocked". The two inputs are "push" and "coin". An output is determined by the current state and the input given at that current state. If the state changes after an input, we call that new state the output. If the state remains the same after an input, we say that there is no outcome. For example, this occurs when you push at a locked turnstile or when you add a coin at an un-locked turnstile.

As programmers, we may use a finite-state machine to help us outline and understand the desired structure and functionalities of our project. 

Within the context of our JavaScript Archery Project, we have 3 states:
- placing the bow
- placing the crosshair
- watching the projectile path

We also have 2 inputs:
- click mouse
- move mouse

In our project, clicking the mouse always results in an outcome while moving the mouse never has an outcome. 

![coffee 'n code, JS archery FSM]()

Sources: 

[1] 

[2] Wikipedia (https://en.wikipedia.org/wiki/Finite-state_machine)
