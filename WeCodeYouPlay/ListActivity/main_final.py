from gamelib import *

game = Game(600,600,"Asteroids")

asteroids = []
for i in range(15):
    a = Animation("images/asteroid_7.png",5,game,510/6,500/5,2)
    x = randint(100,game.width - 100)
    y = randint(100,game.height - 100)
    angle = randint(0,360)
    speed = randint(2,5)
    a.moveTo(x,y)
    a.setSpeed(speed,angle)
    asteroids.append(a)

while not game.over:
    game.processInput()
    game.clearBackground()

    for i in range(len(asteroids)):
        asteroids[i].move(True)

    game.update(30)
game.quit()
