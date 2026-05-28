from microbit import *

while True:
    print( button_a.is_pressed( ) )
    if button_a.is_pressed( ):
        display.show(Image.GHOST)
    elif button_b.is_pressed( ):
        display.show(Image.ANGRY)
    else:
        display.clear()

    sleep(1000)
