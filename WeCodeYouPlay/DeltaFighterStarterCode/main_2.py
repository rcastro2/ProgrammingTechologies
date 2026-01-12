from gamelib import *

#Modular Programming
def hero_update():
    hero.draw()
    if keys.Pressed[K_LEFT]:
        hero.x -= 5
    if keys.Pressed[K_RIGHT]:
        hero.x += 5
    if keys.Pressed[K_UP]:
        hero.y -= 5
    if keys.Pressed[K_DOWN]:
        hero.y += 5  

      
def positionObjects( objects ):
    for i in range(len(objects)):
        x = randint(100,700)
        y = randint(100, 5000)
        objects[i].moveTo(x, -y)
        s = randint(4, 8)
        objects[i].setSpeed(s, 180)
      
game = Game(800,600,"Delta Fighter")
bk = Animation("./images/field_5.png",5,game,1000,1000)
game.setBackground(bk)

hero = Animation("./images/hero2.png",3,game,288 / 3, 96, 2)

asteroids = []
for i in range(50):
    a = Animation("./images/asteroid1t.gif", 41, game, 53, 52)
    asteroids.append(a)
positionObjects(asteroids)

plasmaballs = []
for i in range(20):
    p = Animation("./images/plasmaball1.png", 11, game, 32,  32)
    plasmaballs.append(p)
positionObjects(plasmaballs)

healthpods = []
for i in range(20):
    h = Animation("./images/firstaid.png",40,game,257,250)
    h.resizeBy(-85)
    healthpods.append(h)
positionObjects(healthpods)
    
while not game.over:
    game.processInput()
    game.scrollBackground("down",2)

    hero_update()
    for i in range(len(plasmaballs)):
        plasmaballs[i].move()

    for i in range(len(healthpods)):
        healthpods[i].move()           
  
    for i in range(len(asteroids)):
        asteroids[i].move()
    
    game.update(30)
game.quit()
