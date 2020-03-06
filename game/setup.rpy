label setup:
    "Welcome to Kylatia's Lovely Tutorial and Skill Demo."
#-----------------------------------------------------------------------------------
    # I am storing all homemade screens in character_screen.rpy
    # Right now it's going to do a call so do a call so it pauses the game while you input the name.


    # Sending the variable name and expecting to get it back but stripping off the spaces at the end.
    call screen naming_box("name")
    $name = name.strip ()
    # Name is the only none character stat I'm not keeping in the body at the moment. 


    # If we were doing other setup things like asking favorites this is where I would do it.
    # We can also do other things like call a screen to pick a favorite color or anything else we want the player to set.

#-------------------------------------------------------------------------------------
#return to Script.rpy
return
