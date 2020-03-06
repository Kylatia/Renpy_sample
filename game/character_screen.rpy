# I hate screens and figureing out how to place things but this is what I figured out so far.
screen naming_box (name, done=Return(True)):
    frame:
        xalign .5
        yalign .5
        vbox:
            text _("What is your name?")
            input value VariableInputValue(name,returnable=True)
            
            textbutton _("Confirm"):
                xalign 0.5
                yalign 0.5
                action done
