# Should the Player Choose to come to the Doctor to see about their Ilness.
label hang_with_doctor:
    MC "I really hope the doctor can make me feel better."


    # Resets "daily" and we'll check to see how many times we hit it with a sub label called dr_check before hitting the emptying menu.
    $ player.dr_wait = 0

    # Let's create a menu where you can repeat over and over slowly removes the options already done down.

    # I Declair the Varaible is a set!
    default dr_options = set ()
    default wait_message = "How do you want to entertain yourself.?"

    # Let's Label the menu to send the player back to it as the things finished.

    MC "Waiting at the doctor's office is boring."

    menu office_visit:
        "[wait_message]"
        set dr_options
        "Read a Magazine":
            jump read_mag
        "Play with Phone":
            jump play_with_phone
        "Drink some Water":
            jump drink_water
        "Dance around to the Music":
            jump dance_around

#-------------------------------------------------------------------------------
label dr_ready:
#   We're going to stick this down here to catch the fact the player ran out of options playing with the back button.

    "The doctor will see you now [name]"
    MC "I do love the spoon full of sugar that goes with it."

    jump cycle_body
#-------------------------------------------------------------------------------
#Let's Check to see if the player waited long enough
label dr_check:
    # We're only going to do 3 things off the list, because 0 1 2 
    if player.dr_wait == 2:
        jump dr_ready
    else:
        $wait_message = "What now?"
        $player.dr_wait += 1
    jump office_visit
#-------------------------------------------------------------------------------
label read_mag:
    "Hey this one is from the last year.  Sweet."
    jump dr_check
#-------------------------------------------------------------------------------
label play_with_phone:
    "Beep beep bo beep"
    "Grrr someone's wrong on Twitter, I must argue with them."
    jump dr_check
#-------------------------------------------------------------------------------
label drink_water:
    "Hydration is imporant for blood tests."
    jump dr_check
#-------------------------------------------------------------------------------
label dance_around:
    "Oh yeah this is my jam."
    if player.sickness_level > 2:
        "Oh heck I shouldn't of done that."
    jump dr_check
