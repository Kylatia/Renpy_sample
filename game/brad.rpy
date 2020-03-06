# Should the player choose to jump to see Brad for the day.
label hang_with_brad:
    MC "Brad is just so dreamy."
    if player.sickness_level >= 3:
        MC "And it's not just the feaver talking."
