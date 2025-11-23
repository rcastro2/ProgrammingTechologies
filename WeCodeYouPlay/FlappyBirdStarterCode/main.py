from gamelib import *

game = Game(800,600,"Flappy Bird")
day = Image("./images/day.png",game)
day.resizeTo(game.width, game.height)
game.setBackground( day )


while not game.over:
  game.processInput()

  game.scrollBackground("left",4)
  
  game.update(30)
game.quit()