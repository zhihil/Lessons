# Begin with print statements.
print "Hello world"

# Next, variables.
x = 5       # In this case, '=' is actually like an '<-'
            # x now has the value 5 for the rest of the program.

x = 5 + 2   # Whatever is on the left side of the '=' goes to the left.

print x     # Prints 7



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}} SLIDE 1

# Start with some imports.
import fractals
from fractals import Mandelbrot
from fractals import showImage

# Create a new Mandelbrot OBJECT.
# Mandelbrot is the name of the type of fractal we are creating.
# '()' -> calls
m = Mandelbrot()

# Make the Mandelbrot render. ('.' acts as '->').
pic = m.render()

# Show the result.
showImage(pic)



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}} SLIDE 2

# Start with some imports.
from fractals import Julia

# Create a new Julia OBJECT.
j = Julia()

# Make the Julia render.
pic = j.render()

# Show the result.
showImage(pic)



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}} SLIDE 3

# What if we want the user to decide what to create?
# Let's use the 'input' function.

# Input -> shows a message, gets typed message from user, 
# assigns to 'fractal_type'.
fractal_type = input("What kind of fractal do you want to create?")

print fractal_type

# Now we know what the user wants to do.
# If fractal_type is "Mandelbrot", create a Mandelbrot set.
# Otherwise, if fractal_type is "Julia", create a Julia set.



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}} SLIDE 4

# Input -> shows a message, gets typed message from user, 
# assigns to 'fractal_type'.
fractal_type = input("What kind of fractal do you want to create?")

if fractal_type == "Mandelbrot":
    # Make a new mandelbrot set.
    fractal = Mandelbrot()

elif fractal_type == "Julia":
    fractal = Julia()