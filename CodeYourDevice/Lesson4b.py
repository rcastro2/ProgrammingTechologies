from microbit import *

while True:
    if button_a.is_pressed( ) and button_b.is_pressed( ) :
        display.show(Image.BUTTERFLY)
    elif button_a.is_pressed( ) or button_b.is_pressed( ):
        display.show(Image.DIAMOND)
    else:
        display.clear()

    sleep(1000)
