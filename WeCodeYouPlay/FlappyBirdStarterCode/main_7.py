from gamelib import *

game = Game(800,600,"Flappy Bird")
day = Image("./images/day.png",game)
day.resizeTo(game.width, game.height)
game.setBackground( day )

bird = Animation("./images/bird.png",3,game, 132 / 3, 34, 4)

bar = Animation("./images/bar.png",3,game, 700, 110,3)
bar.resizeTo(game.width, 110)
bar.y = game.height - 50

rings = Animation("./images/ring2.png",64,game, 512 / 8, 512 / 8 )
rings.x = game.width + 100
rings.setSpeed(2,90)

pipetop = Image("./images/pipe_top.png",game)
pipebot = Image("./images/pipe_bot.png",game)

f = Font( red, 48, black, "Comic Sans MS" )

logo = Image("./images/logo.png",game)
logo.y = 100

gameover_logo = Image("./images/flappybird_end.png",game)

#Start Screen
while not game.over:
    game.processInput()
    game.scrollBackground("left",4)
    logo.draw()
    bird.draw()
    bar.draw()

    if keys.Pressed[K_SPACE]:
        game.over = True

    game.drawText("Press [Space] to start", 150, game.height - 80,f)
    game.update(30)

#Game Screen
game.over = False
while not game.over:
  game.processInput()

  game.scrollBackground("left",4)
  bird.draw()
  rings.move()
  pipebot.moveTo(rings.x, rings.y + 200)
  pipetop.moveTo(rings.x, rings.y - 200)
  bar.draw()
  
  if keys.Pressed[K_SPACE]:
    bird.y -= 2
    bird.rotateTo(10)
  else:
    bird.y += 2
    bird.rotateTo(-10)

  if rings.x < -100:
    rings.y = randint(200,300)
    rings.x = game.width + 100
    rings.speed += 1
    rings.visible = True

  if (bird.collidedWith(bar,"rectangle") or 
  bird.collidedWith(pipetop,"rectangle") or 
  bird.collidedWith(pipebot,"rectangle") or
  bird.y < 0):
    game.over = True
    
  if bird.collidedWith( rings ):
          rings.visible = False
          game.score += 1

  game.drawText( game.score, 50, game.height - 75, f )
  game.update(30)

#Game Over Screen
game.over = False
while not game.over:
    game.processInput()
    game.scrollBackground("left",4)
    gameover_logo.draw()
    bird.draw()
    bar.draw()

    if keys.Pressed[K_q]:
        game.over = True

    game.drawText("Press [Q] to quit", 225, game.height - 80,f)
    game.update(30)
game.quit()
