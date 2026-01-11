from gamelib import *

#Game Functions (Modular Programming)
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

#Main Program
game = Game(800,600,"Delta Fighter")
bk = Animation("images/field_5.png",5,game,1000,1000)
game.setBackground(bk)

hero = Animation("images/hero2.png",3,game,288 / 3, 96, 2)
    
while not game.over:
    game.processInput()
    game.scrollBackground("down",2)

    hero_update()

    game.update(30)
game.quit()
