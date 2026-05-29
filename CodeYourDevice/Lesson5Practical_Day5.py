from microbit import *
from random import randint
import audio

hx = 2
hy = 4

ex = randint(0,4)
ey = 0

#Start Screen
gameover = False
while not gameover:
    display.scroll("Dodge Em!")
    
    if button_a.was_pressed() or button_b.was_pressed():
        audio.play(Sound.TWINKLE)
        gameover = True
    
    sleep(100)
    
#Main Screen
gameover = False
score = 0
damage = 0

t = 0
dt = 10
while not gameover:
    display.clear()

    if accelerometer.get_x() > 200 and hx < 4:
        hx += 1
    elif accelerometer.get_x() < -200 and hx > 0:
        hx -= 1
    
    t += 1
    if t == dt:
        ey += 1  
        t = 0
    
    display.set_pixel(hx,hy,9 - damage)
    display.set_pixel(ex,ey,9)
        
    if ex == hx and ey == hy:
        audio.play(Sound.SAD)
        damage += 1
    
    if damage == 3:
        gameover = True
    
    if ey >= 4:
        ey = 0
        ex = randint(0,4)
        score += 1
        if dt > 1:
            dt -= 1
    
    sleep(100)
display.scroll(score)