from microbit import *
from random import randint
import audio
hx = 2
hy = 4
ex = randint(0,4)
ey = 0

#Start Screen
gameover = True
while not gameover:
    display.scroll("Dodge Em!")
    
    if button_a.is_pressed or button_b.is_pressed:
        audio.play(Sound.TWINKLE)
        gameover = True
    
    sleep(100)
#Main Screen
gameover = False
score = 0
dy = 0.2
damage = 0
while not gameover:
    display.clear()
    display.set_pixel(hx,hy,9 - damage)
    display.set_pixel(ex,int(ey),9)

    if accelerometer.get_x() > 200 and hx < 4:
        hx += 1
    elif accelerometer.get_x() < -200 and hx > 0:
        hx -= 1
        
    ey += dy    
    if ex == hx and int(ey) == hy:
        audio.play(Sound.SAD, wait=False)
        damage += 1
        ey = 0
        ex = randint(0,4)
    
    if damage == 3:
        gameover = True
    
    if ey > 4:
        ey = 0
        ex = randint(0,4)
        score += 1
        if dy < 0.9:
            dy += 0.1
    
    sleep(100)
display.scroll(score)
