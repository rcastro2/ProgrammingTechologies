from gamelib import *

game = Game(1024,768,"Hoops Up!")

player1 = Image("player1.png", game)
player1.setSpeed(4,60)
player1.resizeBy(-60)
x = randint(100,900)
y = randint(100,600)
player1.moveTo(x,y)

player2 = Image("player2.png", game)
player2.setSpeed(3,90)
player2.resizeBy(-70)
x = randint(100,900)
y = randint(100,600)
player2.moveTo(x,y)

net = Image("net.png",game)
net.resizeBy(-90)
net.moveTo(512,100)

ball = Image("basketball.png", game)
ball.resizeBy(-95)

court = Image("court.jpg",game)
court.resizeTo(game.width, game.height)

while not game.over:
    game.processInput()

    court.draw()
    net.draw()
    ball.moveTo(mouse.x, mouse.y)

    player1.move(True)
    player2.move(True)

    if ball.collidedWith(net):
        x = randint(100,900)
        y = randint(100,600)
        net.moveTo(x,y)
        game.score += 10
        player1.speed += 1
        player2.speed += 1

    if player1.collidedWith(ball) or player2.collidedWith(ball):
        game.score -= 5
        
    game.drawText("Score: " + str(game.score), 10, 10)
    game.update(30)
game.quit()
