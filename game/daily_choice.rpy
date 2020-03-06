label chores:
    # Checking to see if the player has died yet.
    if player.sickness_level == 0:
        MC "Oh I feel like I'm coming down with something."
        $ player.sickness_level += 1

    # Let's start the daily choice menu.
    menu :
        "What do you want to do?"
        "Hang out with Brad":
            jump hang_with_brad
        "Hang out with Dylan":
            jump hang_with_dylan
        "Go to the Doctor":
            jump hang_with_doctor


    return
