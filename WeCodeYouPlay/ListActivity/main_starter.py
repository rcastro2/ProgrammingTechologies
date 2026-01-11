from gamelib import *

game = Game(600,600,"Asteroids")

#Challenge 1 - Create an empty list for asteroids
for i in range(15):
    x = randint(100,game.width - 100)
    y = randint(100,game.height - 100)
    angle = randint(0,360)
    speed = randint(2,5)
    #Challenge 2 - Create an animation variable for asteroid_7.png

    #Challenge 3 - Move the animation to (x,y)

    #Challenge 4 - Set the speed and angle of the animation

    #Challenge 5 - Add the animation to the asteroids list

while not game.over:
    game.processInput()
    game.clearBackground()

    #Challenge 6 - Create a loop to go through the asteroids

    #Challenge 7 - In the loop, move each asteroid


    game.update(30)
game.quit()
