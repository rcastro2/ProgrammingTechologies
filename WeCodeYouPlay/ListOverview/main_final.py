from gamelib import *

game = Game(600,600,"Super Novas")
suns = []
for i in range(5):
    s = Animation("images/nova.png",5,game,240/3,160/2)
    x = randint(100,game.width - 100)
    y = randint(100,game.height - 100)
    s.moveTo(x,y)
    suns.append(s)

while not game.over:
    game.processInput()
    game.clearBackground()

    for i in range(len(suns)):
        suns[i].draw()

    game.update(30)
game.quit()
