# I like storing the important character stats here instead at the start of script to keep the code cleaner.
# It also allows quick access find what is what.

init python:

    class body:
        def __init__(self):
            # Are you down with the sickness?  How long the player has to find a cure before they die.
            self.sickness_level = 0
            # Let's add love levels for the Love Interests.
            self.love_chad = 0
            self.love_dylan = 0
