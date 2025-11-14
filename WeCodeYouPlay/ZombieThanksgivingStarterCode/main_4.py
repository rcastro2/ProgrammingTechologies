from gamelib import *

game = Game( 800, 600, "Zombie Thanksgiving" )
bk = Image("Zbk.jpg",game)
bk.resizeTo( 800, 600 )

zombie = Image("zombie.png", game)
zombie.resizeBy(-85)
zombie.setSpeed(2,60)

turkey = Image("turkey.gif", game)
turkey.resizeBy(-50)
turkey.setSpeed(3,-45)

crosshair = Image("crosshair.png", game)
crosshair.resizeBy(-70)
crosshair.draw()

while not game.over:
    game.processInput()

    bk.draw()
    zombie.move(True)
    turkey.move(True)
    
    game.update(30)
game.quit()
