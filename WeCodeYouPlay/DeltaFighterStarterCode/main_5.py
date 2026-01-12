from gamelib import *

#Game Functions (Modular Programming)
def hero_update():
    hero.draw()
    healthbar.moveTo( hero.x - 30, hero.y + 50 )
    healthbar.width = hero.health / 2
    ammobar.moveTo( hero.x - 30, hero.y + 70 )
    ammobar.width = hero.ammo * 3
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

#Main Program
game = Game(800,600,"Delta Fighter")
bk = Animation("./images/field_5.png",5,game,1000,1000)
game.setBackground(bk)

hero = Animation("./images/hero2.png",3,game,288 / 3, 96, 2)
hero.ammo = 0
healthbar = Shape("bar",game, hero.health, 10, green)
ammobar = Shape("bar",game, hero.ammo, 10, blue)

explosion = Animation("./images/explosion4.png",20,game,640 / 5, 512 / 4)
explosion.visible = False

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

#Game Loop
while not game.over:
    game.processInput()
    game.scrollBackground("down",2)

    hero_update()
    explosion.draw(False)
    
    for i in range(len(plasmaballs)):
        plasmaballs[i].move()
        if hero.collidedWith( plasmaballs[i]):
          hero.ammo += 1
          plasmaballs[i].visible = False

    for i in range(len(healthpods)):
        healthpods[i].move()   
        if hero.collidedWith( healthpods[ i ]  ):
          hero.health += 5
          healthpods[ i ].visible = False
          
    for i in range(len(asteroids)):
        asteroids[i].move()
        if hero.collidedWith( asteroids[ i ]):
          hero.health -= 10
          asteroids[ i ].visible = False
          explosion.visible = True
          explosion.moveTo( hero.x, hero.y )
    
    game.update(30)
game.quit()
