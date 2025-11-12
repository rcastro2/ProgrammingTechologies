from gamelib import *

game = Game( 800, 600, "Zombie Thanksgiving" )

bk = Image("Zbk.jpg",game)
bk.resizeTo( 800, 600 )
bk.draw()

zombie = Image("zombie.png", game)
zombie.resizeBy(-80)
zombie.draw()

turkey = Image("turkey.gif", game)
turkey.resizeBy(-50)
turkey.draw()

crosshair = Image("crosshair.png", game)
crosshair.resizeBy(-70)
crosshair.draw()

game.update()
