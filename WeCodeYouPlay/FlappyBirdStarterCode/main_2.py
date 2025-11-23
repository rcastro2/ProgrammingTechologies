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
rings.x = 500


while not game.over:
  game.processInput()

  game.scrollBackground("left",4)
  bird.draw()
  bar.draw()
  rings.draw()
  
  game.update(30)
game.quit()
