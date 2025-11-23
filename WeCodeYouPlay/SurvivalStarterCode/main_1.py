from gamelib import *
game = Game(800,600,"Survival")

bk = Image("./images/sand.jpg",game)
bk.resizeTo( game.width, game.height )
game.setBackground( bk )

scorpion = Animation("./images/scorpion.jpg",3,game,288 / 3, 106)
snake = Animation("./images/snake.png",34,game,960 / 5, 1080 / 10)
snake.rotateTo(-90)
bottle = Animation("./images/bottle.png",24, game, 230 / 5, 516 / 5 )
person = Animation("./images/human.png",15,game, 440 / 5, 294 / 3,2)
person.y = game.height - 100

while not game.over:
  game.processInput()

  game.scrollBackground("down",2)
  scorpion.draw()
  bottle.draw()
  snake.draw()
  person.draw()
  person.rotateTo(0)
  
  if keys.Pressed[K_a]:
    person.x -= 4
    person.rotateTo(20)
  if keys.Pressed[K_d]:
    person.x += 4
    person.rotateTo(-20)

  game.update(30)
game.quit()
