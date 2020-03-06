#Dylan and Brad are pretty much the same.

label hang_with_dylan:
    if player.love_dylan == 0:
        MC "Dylan is just so dreamy."
    else:
        MC "I just love spending time with Dylan."
    if player.sickness_level >= 3:
        MC "And it's not just the feaver talking."

# Okay let's work through the love levels for Dylan should the Player chooses to hang with him.
# We can do an if else (ir what ever Renpy uses) block here or we can do an series of if's.  I'm going to go with the if's.

    if player.love_dylan == 0:
        Dylan "Hey, [name].  Let's hang out and do story stuff."
        MC "Oh I love story stuff."
    # We spent time with him before so we're going to spend more time.

    if player.love_dylan == 1:
        Dylan "Oh man [name], I'm happy to see you."
        MC "I just love spending time with you."

    if player.love_dylan == 2:
        MC "I just love spending time with you."
        Dylan "I love spending time with you too."

    if player.love_dylan == 3:
        MC "You are so amazing, Dylan."
        Dylan "And so are you, [name]."

    if player.love_dylan == 4:
        MC "Your so funny and charming, Dylan."
        Dylan "And you are so wonderful."

    if player.love_dylan == 5:
        if player.sickness_level >= 3:
            MC "I know I'm dying but please run away with me and get married so I'll have a few days of happiness before I die."
            Dylan "Of course."
            jump dylan_sick_happy_ending
        if player.sickness_level < 3:
            Dylan "You are doing so amazingly well.  Let's run off and get married."
            MC "OF course!"
            jump dylan_well_happy_ending
    # Why did I pick 5 as a magic number, beats me.
    #Let's add 1 to the love level and the sickness level because the player didn't work on getting better.
    $ player.love_dylan += 1
    $ player.sickness_level += 1

    jump cycle_body # end of day let's go back to the main script.
#-------------------------------------------------------------------------------
label dylan_sick_happy_ending:
    MC "I'm so happy I can spend my final hours with you, Dylan."
    Dylan "I'm glad to be with you too.  So I'm on the life insurnce policy right?"
    MC "Of course."
    # fin
    return
#-------------------------------------------------------------------------------
label dylan_well_happy_ending:
    MC "I love you so much we're ging to go live happily ever after."
    Dylan "Of course."
    return
