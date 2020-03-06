# Let's let the player pick the name they want to see for the character and now MC is the Player Story.
# The default will be Mary Sue until the player gets a chance to change it.
default name = "Mary Sue"
define MC = Character("[name]")

# Personally I love longer variable names so I know exactly what I'm looking at and not just a B D for character speaking.
define Brad = Character("Brad")
define Dylan = Character("Dylan")


#-------------------------------------------------------------------------------
# Game Starts here after what I call the define block to set up the characters.
label start:

    # Let's give the Player a body.  This calling body in Character.rpy
    # Don't you love Python Structures? I do.
    python:
        player = body()

# Now Let's keep this Script clean and jump off to setup.rpy where we can put setup stuff.
# I'm going to call this so when the setup is done it will come back here.
    call setup

# I'm going to set up a Daily Choice for the Player that jumps into a series of If Statments for levels of stuff.
# For example if the Designer wants to have the MC choose where to spend her time during the day to meet different folk.

# Let's call the Label 'chores' in the daily_choice.rpy file.

label cycle_body:

    jump chores



    return
