from gamelib import *

game = Game(1024,768,"Hoops Up!")

player1 = Image("player1.png", game)
player1.setSpeed(4,60)
player1.resizeBy(-60)

player2 = Image("player2.png", game)
player2.setSpeed(3,90)
player2.resizeBy(-70)

ball = Image("basketball.png", game)
ball.resizeBy(-95)

court = Image("court.jpg",game)
court.resizeTo(game.width, game.height)

while not game.over:
    game.processInput()

    court.draw()
    ball.moveTo(mouse.x, mouse.y)

    player1.move(True)
    player2.move(True)

    game.update(30)
game.quit()