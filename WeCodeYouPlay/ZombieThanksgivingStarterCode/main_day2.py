from gamelib import *

game = Game( 800, 600, "Zombie Thanksgiving" )
bk = Image("Zbk.jpg",game)
bk.resizeTo( 800, 600 )
bk.draw()
zombie = Image("zombie.png", game)
zombie.resizeBy(-80)
zombie.draw()
game.update()