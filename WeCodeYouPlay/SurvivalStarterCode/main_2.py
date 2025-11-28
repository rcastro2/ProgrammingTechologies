from gamelib import *
game = Game(800,600,"Survival")

bk = Image("./images/sand.jpg",game)
bk.resizeTo( game.width, game.height )
game.setBackground( bk )

scorpion = Animation("./images/scorpion.jpg",3,game,288 / 3, 106)
scorpion.y = -randint(10, 200)
scorpion.x = randint(100, 700)
scorpion.setSpeed(2,180)
snake = Animation("./images/snake.png",34,game,960 / 5, 1080 / 10)
snake.rotateTo(-90)
snake.y = -randint(10, 200)
snake.x = randint(100, 700)
snake.setSpeed(2,180)

bottle = Animation("./images/bottle.png",24, game, 230 / 5, 516 / 5 )
bottle.y = -randint(10, 200)
bottle.x = randint(100, 700)
bottle.setSpeed(2,180)
person = Animation("./images/human.png",15,game, 440 / 5, 294 / 3,2)
person.y = game.height - 100

f1 = Font(black, 36, red, "Arial")
f2 = Font(black, 18, red, "Arial")

while not game.over:
  game.processInput()

  game.scrollBackground("down",2)
  scorpion.move()
  bottle.move()
  snake.move()
  person.draw()
  person.rotateTo(0)
  if(keys.Pressed[K_a]):
    person.x -= 4
    person.rotateTo(20)
  if(keys.Pressed[K_d]):
    person.x += 4
    person.rotateTo(-20)

  if bottle.y > game.height + 100:
    bottle.y = -randint(10, 200)
    bottle.x = randint(100, 700)

  if scorpion.y > game.height + 100:
    scorpion.y = -randint(10, 200)
    scorpion.x = randint(100, 700)
    scorpion.speed += 1

  if snake.y > game.height + 100:
    snake.y = -randint(10, 200)
    snake.x = randint(100, 700)
    scorpion.speed += 2

  if snake.collidedWith(person) or scorpion.collidedWith(person):
    person.health -= 1

  if person.collidedWith(bottle):
    bottle.y = -randint(10, 200)
    bottle.x = randint(100, 700)
    game.score += 10

  if person.health <= 0:
    game.over = True

  game.drawText(person.health, person.x-10, person.y + 50,f2)
  game.drawText(game.score, 50, 50, f1)
  game.update(30)
game.wait(K_SPACE)
game.quit()
