# Dylan and Brad are pretty much the same.

label hang_with_brad:
    if player.love_brad == 0:
        MC "Brad is just so dreamy."
    else:
        MC "I just love spending time with Brad."
    if player.sickness_level >= 3:
        MC "And it's not just the feaver talking."

# Okay let's work through the love levels for brad should the Player chooses to hang with him.
# We can do an if else (ir what ever Renpy uses) block here or we can do an series of if's.  I'm going to go with the if's.

    if player.love_brad == 0:
        Brad "Hey, [name].  Let's hang out and do story stuff."
        MC "Oh I love story stuff."
    # We spent time with him before so we're going to spend more time.

    if player.love_brad == 1:
        Brad "Oh man [name], I'm happy to see you."
        MC "I just love spending time with you."

    if player.love_brad == 2:
        MC "I just love spending time with you."
        Brad "I love spending time with you too."

    if player.love_brad == 3:
        MC "You are so amazing, brad."
        Brad "And so are you, [name]."

    if player.love_brad == 4:
        MC "Your so funny and charming, Brad."
        Brad "And you are so wonderful."

    if player.love_brad == 5:
        if player.sickness_level >= 3:
            MC "I know I'm dying but please run away with me and get married so I'll have a few days of happiness before I die."
            Brad "Of course."
            jump brad_sick_happy_ending
        if player.sickness_level < 3:
            brad "You are doing so amazingly well.  Let's run off and get married."
            MC "OF course!"
            jump brad_well_happy_ending
    # Why did I pick 5 as a magic number, beats me.
    #Let's add 1 to the love level and the sickness level because the player didn't work on getting better.
    $ player.love_brad += 1
    $ player.sickness_level += 1

    jump cycle_body # end of day let's go back to the main script.

label brad_sick_happy_ending:
    MC "I'm so happy I can spend my final hours with you, Brad."
    Brad "I'm glad to be with you too.  So I'm on the life insurnce policy right?"
    MC "Of course."
    return
label brad_well_happy_ending:
    MC "I love you so much we're ging to go live happily ever after."
    Brad "Of course."
    return
