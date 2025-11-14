from gamelib import *

game = Game( 800, 600, "Zombie Thanksgiving" )

bk = Image("Zbk.jpg",game)
bk.resizeTo(800,600)

zombie = Image("zombie.png",game)
zombie.resizeBy(-90)
zombie.setSpeed(2,60)

turkey = Image("turkey.gif",game)
turkey.resizeBy(-65)
turkey.setSpeed(3,-45)

crosshair = Image("crosshair.png",game)
crosshair.resizeBy(-85)

while not game.over:
    game.processInput()

    bk.draw()
    zombie.move(True)
    turkey.move(True)

    if zombie.collidedWith( turkey  ):
      x = randint(  100, 700  )
      y = randint(  100, 500  )
      turkey.moveTo( x, y )

    if mouse.collidedWith( zombie  ):
      x = randint(  100, 700  )
      y = randint(  100, 500  )
      zombie.moveTo( x, y )

    crosshair.moveTo(mouse.x, mouse.y)
 
    game.update(30)
game.quit()